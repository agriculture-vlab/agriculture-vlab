# The MIT License (MIT)
# Copyright (c) 2021-2022 by the ESA AVL development team and contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

"""The _admin module provides utilities for AVL infrastructure configuration

This module is intended for the use of AVL system administrators and is not
relevant to users.
"""

import json
from datetime import datetime
from typing import Tuple
import logging

import boto3
import boto3.session

PERMISSIONS_BOUNDARY = "user-permissions-boundary"
BUCKET_ACCESS_USER_PREFIX = "s3-user"


class AwsResourceCreator:
    """A class to create the AWS resources necessary to run the AVL

    This class automatically creates and configures the buckets needed by the
    AVL, as well as an IAM "user manager" user with restricted permissions to
    create IAM bucket access users, and a policy to be used as a permissions
    boundary for the bucket access users.
    """

    def __init__(self, aws_account_number: str, creator_tag: str,
                 resource_prefix: str):
        """Instantiate a new AWS resource creator.

        No AWS resources are created until the create_resources method
        is called.

        :param aws_account_number: number of AWS account under which resources
               are to be created
        :param creator_tag: value for the "creator" tag in created resources
        :param resource_prefix: prefix to apply to name of created resources
        """
        # We assume that a suitable access key and secret are specified
        # in .aws/credentials or the equivalent environment variables where
        # boto3 can find them.
        self.resource_prefix = resource_prefix
        self.region = "eu-central-1"
        self.session = boto3.session.Session(region_name="eu-central-1")
        self.iam_client = self.session.client(service_name="iam")
        self.s3_client = self.session.client(service_name="s3")
        self.tags = [
            dict(Key="creator", Value=creator_tag),
            dict(
                Key="create-date", Value=datetime.now().strftime(r"%Y-%m-%d")
            ),
            dict(Key="project", Value="avl"),
        ]
        self.aws_account_number = aws_account_number
        self.aws_account_id = "arn:aws:iam::" + aws_account_number
        self.user_manager_key_id = None
        self.user_manager_key_secret = None

    def create_resources(self):
        """Create all the resources required by AVL"""
        self.create_buckets()
        self.create_users_and_policies()

    def create_buckets(self):
        """Create and configure the S3 buckets required by AVL"""
        bucket_ids = ["user", "data", "data-test", "data-staging", "scratch"]

        # Create standard AVL buckets
        for bucket_id in bucket_ids:
            bucket_name = self.resource_prefix + "-" + bucket_id
            self.s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    "LocationConstraint": "eu-central-1"
                },
                ObjectOwnership="BucketOwnerEnforced",
            )
            self.s3_client.put_bucket_tagging(Bucket=bucket_name,
                                              Tagging=dict(TagSet=self.tags))

        # Apply lifecycle policy to scratch bucket
        self.s3_client.put_bucket_lifecycle_configuration(
            Bucket=self.resource_prefix + "-scratch",
            LifecycleConfiguration={
                "Rules": [{
                    "Expiration": {"Days": 2},
                    "ID": "delete-old-objects",
                    "Filter": {},
                    "Status": "Enabled",
                    "AbortIncompleteMultipartUpload":
                        {"DaysAfterInitiation": 1}}
                ]},
        )

    def create_users_and_policies(self):
        """Create IAM users and policies required by AVL"""
        # Create permissions boundary to restrict capabilities of
        # dynamically created bucket users.
        self.iam_client.create_policy(
            PolicyName=self.resource_prefix + "-" + PERMISSIONS_BOUNDARY,
            PolicyDocument=json.dumps(
                {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Sid": "AllowedOperations",
                            "Effect": "Allow",
                            "Action": [
                                "s3:AbortMultipartUpload",
                                "s3:DeleteObject*",
                                "s3:GetObject*",
                                "s3:ListBucket",
                                "s3:ListMultipartUploadParts",
                                "s3:PutObject*"
                            ],
                            "Resource": [
                                f"arn:aws:s3:::{self.resource_prefix}-user",
                                f"arn:aws:s3:::{self.resource_prefix}-user/*",
                            ],
                        }
                    ],
                }
            ),
            Description="Limit permissions for AVL bucket access users",
            Tags=self.tags
            + [
                dict(
                    Key="purpose",
                    Value="Limit permissions for AVL bucket access users",
                )
            ],
        )

        # Create "user manager" IAM user (used to create the dynamic
        # bucket users)
        user_manager_username = f"{self.resource_prefix}-user-manager"
        self.iam_client.create_user(
            UserName=user_manager_username, Tags=self.tags
        )

        # Apply a restrictive policy to the "user manager" user. This policy
        # restricts operations to user IDs under the AVL path, and forces the
        # user manager to apply the permissions boundary to any users it
        # creates, so it can't escalate its permissions by creating more
        # powerful users.
        user_pattern = f"{self.aws_account_id}:user/{self.resource_prefix}-" \
                       f"{BUCKET_ACCESS_USER_PREFIX}/*"
        self.iam_client.put_user_policy(
            UserName=user_manager_username,
            PolicyName="aws-user-manager-policy",
            PolicyDocument=json.dumps(
                {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Sid": "CreateUsersWithBoundaryAndPath",
                            "Effect": "Allow",
                            "Action": ["iam:CreateUser"],
                            "Resource": user_pattern,
                            "Condition": {
                                "StringEquals": {
                                    "iam:PermissionsBoundary":
                                        f"{self.aws_account_id}:policy/"
                                        f"{self.resource_prefix}-"
                                        f"{PERMISSIONS_BOUNDARY}"
                                }
                            },
                        },
                        {
                            "Sid": "ManageUsersUnderPath",
                            "Effect": "Allow",
                            "Action": [
                                "iam:CreateAccessKey",
                                "iam:DeleteAccessKey",
                                "iam:DeleteUser",
                                "iam:GetUser",
                                "iam:ListAccessKeys",
                                "iam:PutUserPolicy",
                                "iam:TagUser"
                            ],
                            "Resource": user_pattern,
                        },
                        {
                            "Sid": "ListUsers",
                            "Effect": "Allow",
                            "Action": ["iam:ListUsers"],
                            "Resource": "*",
                        },
                    ],
                }
            ),
        )

        # Create and store credentials for the "user manager" user.
        access_key = self.iam_client.create_access_key(
            UserName=user_manager_username)
        self.user_manager_key_id = access_key["AccessKey"]["AccessKeyId"]
        self.user_manager_key_secret = access_key["AccessKey"][
            "SecretAccessKey"]


class BucketAccessUserCreator:
    """Create IAM users and credentials for AVL S3 bucket access

    This class is intended to be used by the Jupyter Hub process when
    spawning a new user environment. It creates (if not already present) an
    IAM user with permissions to read and write to the AVL user's prefix in
    the user bucket, and creates and returns access credentials for this IAM
    user, which the Jupyter Hub process can then pass to the user environment
    in environment variables. In this documentation, this IAM user is termed
    the "bucket access user".

    The design of this class allows for the IAM users to be periodically
    culled or manually deleted if no corresponding user session is currently
    active; the ensure_user_and_create_key method will reuse the existing
    user if it is present, and create a new one on the fly if not. New access
    credentials are always created; if any access credentials are already
    present, the most recently created set will be kept in addition to the
    new credentials.
    """

    def __init__(self, user_name: str, client_id: str, client_secret: str,
                 aws_account_number: str, creator_tag: str,
                 resource_prefix: str):
        """Instantiate a new bucket access user creator

        No user or access key is created until the ensure_user_and_create_key
        method is called.

        :param user_name: the AVL user name, which will be used as one
               component of the IAM user name
        :param client_id: the client ID of the IAM user that will be used to
               create the bucket access user. It is expected that this will be
               the "user manager" user created during AVL initialization, but
               any user with sufficient permissions will work.
        :param client_secret: the client secret associated with the client_id
               parameter
        :param aws_account_number: the number of the AWS account hosting the
               AVL
        :param creator_tag: the value to be used for the "creator" tag applied
               to the bucket access user
        :param resource_prefix: prefix to use when constructing the IAM user
               name from the AVL user name
        """
        self.user_name = user_name
        self.resource_prefix = resource_prefix
        self.iam_user_name = f"{self.resource_prefix}-" \
                             f"{BUCKET_ACCESS_USER_PREFIX}-{self.user_name}"
        self.aws_account_number = aws_account_number
        self.client = boto3.client(
            service_name="iam",
            region_name="eu-central-1",
            aws_access_key_id=client_id,
            aws_secret_access_key=client_secret
        )
        self.tags = [
            dict(Key="creator", Value=creator_tag),
            dict(
                Key="create-date", Value=datetime.now().strftime(r"%Y-%m-%d")
            ),
            dict(Key="project", Value="avl"),
        ]

    def ensure_user_and_create_key(self) -> Tuple[str, str]:
        """Create an IAM user for bucket access (if needed) and access key

        If the IAM user does not exist, it is created. A new access key and
        secret are always created and returned. If the user already exists
        and has more than one existing access key and secret, all but the
        most recently created key/secret pairs are deleted before creating
        the new key/secret pair.

        Returns a tuple consisting of a valid access key and access secret
        for the bucket access user.
        """
        boundary_arn = f"arn:aws:iam::{self.aws_account_number}:" \
                       f"policy/{self.resource_prefix}-{PERMISSIONS_BOUNDARY}"
        try:
            logging.info(f"Trying to create new IAM user {self.iam_user_name}.")
            self.client.create_user(
                Path=f"/{self.resource_prefix}-{BUCKET_ACCESS_USER_PREFIX}/",
                UserName=self.iam_user_name,
                PermissionsBoundary=boundary_arn,
                Tags=self.tags
            )
        except self.client.exceptions.EntityAlreadyExistsException:
            logging.info(f"User {self.iam_user_name} exists; creating new "
                         f"credentials for existing user.")
            # AWS allows maximum two keys per user, so we make sure that
            # we have at most one before trying to create any more.
            self.delete_oldest_access_keys()
        self.add_policy()

        user_key_id, user_key_secret = self.create_access_key()
        return user_key_id, user_key_secret

    def delete_oldest_access_keys(self):
        """Delete all but the most recent access key for the IAM user"""
        list_response = self.client.list_access_keys(
            UserName=self.iam_user_name)
        sorted_keys = sorted(list_response["AccessKeyMetadata"],
                             key=lambda x: x["CreateDate"])
        for key_record in sorted_keys[:-1]:
            # Delete all but the most recently created key.
            # We don't expect >2 in total, but supporting it requires no
            # additional code.
            key_id = key_record["AccessKeyId"]
            logging.info(f"Deleting old access key {key_id} for "
                         f"{self.iam_user_name}.")
            self.client.delete_access_key(
                UserName=self.iam_user_name,
                AccessKeyId=key_id
            )

    def create_access_key(self):
        """Create and return an access key/secret pair for the IAM user"""
        user_key = self.client.create_access_key(UserName=self.iam_user_name)
        user_key_id = user_key["AccessKey"]["AccessKeyId"]
        user_key_secret = user_key["AccessKey"]["SecretAccessKey"]
        return user_key_id, user_key_secret

    def add_policy(self):
        """Apply an inline access policy to the IAM bucket access user

        The policy added by this method allows some standard S3 operations
        and restricts AVL user bucket access to paths with the user's own
        prefix. Note that the user's capabilities are also restricted by the
        permissions boundary applied on user creation.
        """
        user_name = self.user_name
        policy = json.dumps({
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "AllowList",
                    "Effect": "Allow",
                    "Action": ["s3:ListBucket"],
                    "Resource": [
                        f"arn:aws:s3:::{self.resource_prefix}-user",
                        f"arn:aws:s3:::{self.resource_prefix}-user/{user_name}",
                        f"arn:aws:s3:::{self.resource_prefix}-"
                        f"user/{user_name}/*"
                    ],
                    "Condition": {
                        "ForAllValues:StringLike": {
                            "s3:prefix": [f"{user_name}/", f"{user_name}/*"]
                        }
                    }
                },
                {
                    "Sid": "AllowSomeOperations",
                    "Effect": "Allow",
                    "Action": [
                        "s3:AbortMultipartUpload",
                        "s3:DeleteObject*",
                        "s3:GetObject*",
                        "s3:ListMultipartUploadParts",
                        "s3:PutObject*"
                    ],
                    "Resource": [
                        f"arn:aws:s3:::{self.resource_prefix}-user/{user_name}",
                        f"arn:aws:s3:::{self.resource_prefix}-"
                        f"user/{user_name}/*"
                    ]
                }
            ]
        })
        self.client.put_user_policy(
            UserName=self.iam_user_name,
            PolicyName="avl-buckets-user-access-policy",
            PolicyDocument=policy
        )
