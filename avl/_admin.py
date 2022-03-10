# The MIT License (MIT)
# Copyright (c) 2021 by the ESA AVL development team and contributors
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

import json
from datetime import datetime
from typing import Tuple

import boto3
import boto3.session

PERMISSIONS_BOUNDARY = "user-permissions-boundary"
BUCKET_ACCESS_USER_PREFIX = "s3-user"


class AwsResourceCreator:
    def __init__(self, aws_account_number: str, creator_tag: str,
                 resource_prefix: str):
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
        self.create_buckets()
        self.create_users_and_policies()

    def create_buckets(self):
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
                                "s3:ListMultipartUploadParts",
                                "s3:DeleteObject*",
                                "s3:GetObject*",
                                "s3:PutObject*",
                                "s3:ListBucket",
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
        # forces the user manager to apply the permissions boundary to any
        # users it creates, so it can't escalate its permissions by creating
        # more powerful users.
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
                            "Resource": f"{self.aws_account_id}:user/"
                                        f"avl-bucket-user/*",
                            "Condition": {
                                "StringEquals": {
                                    "iam:PermissionsBoundary":
                                        f"{self.aws_account_id}:policy/"
                                        f"{PERMISSIONS_BOUNDARY}"
                                }
                            },
                        },
                        {
                            "Sid": "ManageUsersUnderPath",
                            "Effect": "Allow",
                            "Action": [
                                "iam:GetUser",
                                "iam:DeleteUser",
                                "iam:PutUserPolicy",
                                "iam:CreateAccessKey",
                                "iam:DeleteAccessKey",
                            ],
                            "Resource": f"{self.aws_account_id}:user/"
                                        f"{self.resource_prefix}-bucket-user/*",
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

    def __init__(self, user_name: str, client_id: str, client_secret: str,
                 aws_account_number: str, creator_tag: str,
                 resource_prefix: str):
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

    def create_user(self) -> Tuple[str, str]:
        boundary_arn = f"arn:aws:iam::{self.aws_account_number}:" \
                       f"policy/{PERMISSIONS_BOUNDARY}"
        print(boundary_arn)
        try:
            self.client.create_user(
                Path=f"/{self.resource_prefix}-{BUCKET_ACCESS_USER_PREFIX}/",
                UserName=self.iam_user_name,
                PermissionsBoundary=boundary_arn,
                Tags=self.tags
            )
        except self.client.exceptions.EntityAlreadyExistsException:
            print("User exists; creating new credentials for existing user.")
            # AWS allows maximum two keys per user, so we make sure that
            # we have at most one.
            self.delete_oldest_access_keys()
        self.add_policy()

        user_key_id, user_key_secret = self.create_access_key()
        return user_key_id, user_key_secret

    def delete_oldest_access_keys(self):
        list_response = self.client.list_access_keys(
            UserName=self.iam_user_name)
        sorted_keys = sorted(list_response["AccessKeyMetadata"],
                             key=lambda x: x["CreateDate"])
        for key_record in sorted_keys[:-1]:
            # Delete all but the most recently created key.
            # We don't expect >2 in total, but supporting it requires no
            # additional code.
            self.client.delete_access_key(
                UserName=self.iam_user_name,
                AccessKeyId=key_record["AccessKeyId"]
            )
        print(sorted_keys)

    def create_access_key(self):
        user_key = self.client.create_access_key(UserName=self.iam_user_name)
        user_key_id = user_key["AccessKey"]["AccessKeyId"]
        user_key_secret = user_key["AccessKey"]["SecretAccessKey"]
        return user_key_id, user_key_secret

    def add_policy(self):
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
                        "s3:ListMultipartUploadParts",
                        "s3:DeleteObject*",
                        "s3:GetObject*",
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
