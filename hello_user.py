import json


def hello_user_handler(event, context):
    return {"statusCode": 200, "body": json.dumps({"message": "Hello ntihsih!"})}
