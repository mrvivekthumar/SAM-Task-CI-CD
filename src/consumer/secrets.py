import json
import os

import boto3


secrets_client = boto3.client("secretsmanager")


def get_secret():

    secret_name = os.environ["SECRET_NAME"]

    response = secrets_client.get_secret_value(
        SecretId=secret_name
    )

    return json.loads(response["SecretString"])
