import json

from consumer.secrets import get_secret
from consumer.service import process_message


def lambda_handler(event, context):

    print(f"Received event: {json.dumps(event)}")

    secret = get_secret()

    print(f"Loaded Secret: {secret}")

    for record in event["Records"]:

        message = json.loads(record["body"])

        print(f"Processing Message: {message}")

        response = process_message(
            message=message,
            secret=secret
        )

        print(f"Processed Response: {response}")

    return {
        "statusCode": 200,
        "body": json.dumps("Messages processed successfully")
    }
