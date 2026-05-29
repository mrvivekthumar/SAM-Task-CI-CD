import json

from consumer.service import process_message


def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    for record in event["Records"]:
        body = json.loads(record["body"])

        response = process_message(body)

        print("Processed Response:", response)

    return {
        "statusCode": 200,
        "body": json.dumps("Messages processed successfully")
    }
