import boto3
from SendGridEventClass import SendGridEvent

dynamo = boto3.client('dynamodb')

def dynamo_handler(payloads):
    for payload in payloads:
        e = SendGridEvent()
        e.add_event(payload)
        
        dynamo.put_item(
            TableName=e.TableName,
            Item=e.Item
        )