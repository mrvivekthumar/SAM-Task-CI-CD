import requests

from consumer.secrets import get_secret


def process_message(message):

    secret = get_secret()

    print("Loaded Secret:", secret)

    print("Processing message:", message)

    response = requests.get("https://httpbin.org/get")

    return {
        "message": message,
        "status_code": response.status_code,
        "secret_loaded": True
    }