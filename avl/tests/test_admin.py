import os
from avl import _admin
import boto3
from moto import mock_s3, mock_iam


@mock_s3
@mock_iam
def test_create_resources():
    
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"

    creator = _admin.AwsResourceCreator(aws_account_number="000000000000")
    creator.create_resources()

    s3_client = boto3.client("s3")
    bucket_response = s3_client.list_buckets()
    buckets = sorted([bucket["Name"] for bucket in bucket_response["Buckets"]])
    assert ["agriculture-vlab-data",
            "agriculture-vlab-data-staging",
            "agriculture-vlab-data-test",
            "agriculture-vlab-scratch",
            "agriculture-vlab-user"] == buckets
    assert len(s3_client.get_bucket_lifecycle_configuration(
        Bucket="agriculture-vlab-scratch")["Rules"]) > 0

    iam_client = boto3.client("iam")
    users_response = iam_client.list_users()
    users = [u["UserName"] for u in users_response["Users"]]
    assert ["avl-iam-user-manager"] == users

    policies_response = iam_client.list_policies(Scope="Local")
    policies = [p["PolicyName"] for p in policies_response["Policies"]]
    assert ["avl-user-permissions-boundary"] == policies

    policy_response = iam_client.get_user_policy(
        UserName="avl-iam-user-manager",
        PolicyName="aws-user-manager-policy"
    )
    assert len(policy_response["PolicyDocument"]) > 0


@mock_iam
def test_bucket_access_user_creator():
    # TODO
    pass
