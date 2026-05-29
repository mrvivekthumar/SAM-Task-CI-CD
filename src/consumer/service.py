import boto3


ses_client = boto3.client("ses")


def process_message(message, secret):

    sender_email = secret["sender_email"]

    receiver_email = secret["receiver_email"]

    ses_client.send_email(
        Source=sender_email,
        Destination={
            "ToAddresses": [
                receiver_email
            ]
        },
        Message={
            "Subject": {
                "Data": "SQS Message Processed"
            },
            "Body": {
                "Text": {
                    "Data": f"Processed message: {message}"
                }
            }
        }
    )

    return {
        "message": message,
        "status_code": 200,
        "email_sent": True
    }
