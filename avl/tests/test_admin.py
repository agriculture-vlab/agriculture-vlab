import json
import os
import time
from datetime import datetime
from typing import List

import boto3
import pytest
from moto import mock_aws

from avl import _admin
from avl._admin import BucketAccessUserCreator


@mock_aws
class TestAdmin:

    @pytest.fixture(autouse=True)
    def env_vars(self):
        # The @mock_aws decorator *should* make the environment variables
        # superfluous, but best to play it safe to avoid any danger of
        # manipulating real AWS resources by mistake.

        for aws_var in ['ACCESS_KEY_ID', 'SECRET_ACCESS_KEY', 'SECURITY_TOKEN',
                        'SESSION_TOKEN']:
            os.environ[f'AWS_{aws_var}'] = 'testing'

    def test_create_resources(self):
        creator_tag = 'creator_name'
        resource_prefix = 'avltest'
        alert_email = 'test@example.com'
        bucket_size_limit = 12345
        creator = _admin.AwsResourceCreator(
            aws_account_number='000000000000',
            creator_tag=creator_tag,
            resource_prefix=resource_prefix,
            alert_email=alert_email,
            bucket_size_limit_bytes=bucket_size_limit
        )
        creator.create_resources()

        s3_client = boto3.client('s3')
        bucket_response = s3_client.list_buckets()
        expected_buckets = [resource_prefix + '-' + name for name in
                            ['data', 'data-staging', 'data-test', 'public',
                             'scratch', 'user']]
        buckets = sorted([bucket['Name']
                          for bucket in bucket_response['Buckets']])
        assert expected_buckets == buckets
        assert len(s3_client.get_bucket_lifecycle_configuration(
            Bucket=f'{resource_prefix}-scratch')['Rules']) > 0
        for bucket in expected_buckets:
            assert {'creator': creator_tag,
                    'project': 'avl',
                    'cost-center': 'avl',
                    'create-date': datetime.now().strftime(r'%Y-%m-%d')} == \
                   _boto_dict_to_dict(s3_client.get_bucket_tagging(
                       Bucket=bucket)['TagSet'])

        iam_client = boto3.client('iam')
        users_response = iam_client.list_users()
        users = [u['UserName'] for u in users_response['Users']]
        assert [f'{resource_prefix}-user-manager'] == users

        policies_response = iam_client.list_policies(Scope='Local')
        policies = [p['PolicyName'] for p in policies_response['Policies']]
        assert [f'{resource_prefix}-{_admin.PERMISSIONS_BOUNDARY}'] == policies
        policy_response = iam_client.get_user_policy(
            UserName=f'{resource_prefix}-user-manager',
            PolicyName='aws-user-manager-policy'
        )
        assert len(policy_response['PolicyDocument']) > 0

        cloudwatch_client = boto3.client('cloudwatch',
                                         region_name='eu-central-1')
        cloudwatch_response = cloudwatch_client.describe_alarms()
        metric_alarms = cloudwatch_response['MetricAlarms']
        assert 3 == len(metric_alarms)
        for metric_alarm in metric_alarms:
            assert 'BucketSizeBytes' == metric_alarm['MetricName']
            assert 'Average' == metric_alarm['Statistic']
            assert bucket_size_limit == metric_alarm['Threshold']

        sns_client = boto3.client('sns', region_name='eu-central-1')
        topics = sns_client.list_topics()['Topics']
        assert 1 == len(topics)
        topic_arn = topics[0]['TopicArn']
        subscriptions = sns_client.list_subscriptions()["Subscriptions"]
        assert 1 == len(subscriptions)
        subscription = subscriptions[0]
        assert topic_arn == subscription['TopicArn']
        assert 'email' == subscription['Protocol']
        assert alert_email == subscription['Endpoint']

    def test_bucket_access_user_creator(self):
        resource_prefix = 'avltest'
        creator_tag = 'creator_name'
        user_name = 'bob'
        iam_client = boto3.client('iam')

        policy = self._create_boundary_policy(iam_client)
        creator = BucketAccessUserCreator(user_name=user_name,
                                          client_id='AKIA-dummy',
                                          client_secret='dummy',
                                          aws_account_number='123456789012',
                                          creator_tag=creator_tag,
                                          resource_prefix='avltest')
        access_id, access_secret = creator.ensure_user_and_create_key()
        assert isinstance(access_id, str)
        assert isinstance(access_secret, str)

        user_response = iam_client.get_user(
            UserName=f'{resource_prefix}-{_admin.BUCKET_ACCESS_USER_PREFIX}-'
                     f'{user_name}')

        # We have to skip the check for the correctly applied permissions
        # boundary, since moto (as of version 3.0.5) only supports permissions
        # boundaries for roles, not for users.

        assert {'creator': creator_tag,
                'project': 'avl',
                'cost-center': 'avl',
                'create-date': datetime.now().strftime(r'%Y-%m-%d')} == \
               _boto_dict_to_dict(user_response['User']['Tags'])

    def test_bucket_access_user_creator_with_existing_credentials(self):
        resource_prefix = 'avltest'
        user_name = 'fred'
        iam_client = boto3.client('iam')
        self._create_boundary_policy(iam_client)
        creator_tag = 'thecreator'
        creator = BucketAccessUserCreator(user_name=user_name,
                                          client_id='AKIA-dummy',
                                          client_secret='dummy',
                                          aws_account_number='123456789012',
                                          creator_tag=creator_tag,
                                          resource_prefix=resource_prefix)
        creator.ensure_user_and_create_key()
        time.sleep(1)  # make sure the keys have distinct CreateDates
        access_id_2, _ = creator.ensure_user_and_create_key()
        access_id_3, _ = creator.ensure_user_and_create_key()

        list_response = iam_client.list_access_keys(
            UserName=f'{resource_prefix}-'
                     f'{_admin.BUCKET_ACCESS_USER_PREFIX}-{user_name}')

        assert {access_id_2, access_id_3} ==\
               {record['AccessKeyId']
                for record in list_response['AccessKeyMetadata']}

    @staticmethod
    def _create_boundary_policy(iam_client):
        return iam_client.create_policy(
            PolicyName=_admin.PERMISSIONS_BOUNDARY,
            PolicyDocument=json.dumps(
                {
                    'Version': '2012-10-17',
                    'Statement': [
                        {
                            'Sid': 'AllowedOperations',
                            'Effect': 'Allow',
                            'Action': [
                                's3:ListBucket',
                            ],
                            'Resource': [
                                'arn:aws:s3:::agriculture-vlab-user',
                            ],
                        }
                    ],
                }
            ),
        )


def _boto_dict_to_dict(boto_dict: List) -> dict:
    return {item['Key']: item['Value'] for item in boto_dict}
