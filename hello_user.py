import json


def hello_user_handler(event, context):
    print(event)
    print(context)
    username = event["queryStringParameters"]["user"]
    return {"statusCode": 200, "body": json.dumps({"message": f"Hello {username}!"})}
