import json
import os
import boto3

sqs = boto3.client("sqs")
QUEUE_URL = os.environ["SQS_QUEUE_URL"]


def lambda_handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method", "POST")

    # Trello exige isso na criação do webhook
    if method == "HEAD":
        return {"statusCode": 200, "body": ""}

    body = event.get("body") or ""

    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=body
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"ok": True})
    }
