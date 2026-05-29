import json
import os
import boto3


def get_secret():

    secret_name = os.environ["SECRET_NAME"]

    client = boto3.client("secretsmanager")

    response = client.get_secret_value(
        SecretId=secret_name
    )

    secret = response["SecretString"]

    return json.loads(secret)