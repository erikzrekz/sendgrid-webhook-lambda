import json
from Dynamo import dynamo_handler
print('Loading function')

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }
    
def lambda_handler(event, context):
    print("Received event!")
    payloads = json.loads(event['body'])
    if (payloads and isinstance(payloads, list)):
        dynamo_handler(payloads)
      
    return respond(None)
