# sendgrid-webhook-lambda
A handler that saves Sendgrid's webhook events into DynamoDB

Requires
- SendGrid
- AWS: API Gateway, Lambda, DynamoDB

## SendGrid
In your SendGrid account, head to https://app.sendgrid.com/settings/mail_settings. Then find Event Notification. This section is where you will tell SendGrid where to POST. (If you don't mind consuming everything, you don't have to pay any attention to those boxes. The lambda handler will handle all of that for you.)

<img width="600px" src="https://i.imgur.com/UpTb5y8.png">

## AWS: API Gateway
Add an POST method endpoint in AWS Gateway. Make sure you choose only the POST method as well as Request Body Validation. While we won't be validating that the body has fields for every type of event, we'll make sure to cover the basics. You can use this JSON Schema to setup a model.

```
{
    "title": "Event",
    "type": "object",
    "properties": {
        "timestamp": {
            "type": "integer"
        },
        "event": {
            "type": "string"
        },
        "email": {
            "type": "string"
        },
        "smtp-id": {
            "type": "string"
        },
        "sg_event_id": {
            "type": "string"
        },
        "sg_message_id": {
            "type": "string"
        }
    },
    "required": ["event", "timestamp", "email", "smtp-id", "sg_event_id", "sg_message_id"]
}
```

## AWS: Lambda
Import the files in this repo for the handler and the two imports.

## AWS: DynamoDB
The only thing that I did to setup a DB was choose `sg_event_id` as the primary key and `timestamp` as the sort key. 

### Testing
Once you're all set up, grab yourself an API key in SendGrid, the URL that you made in API Gateway, and test it with cURL. 

```
curl --request POST   --url https://api.sendgrid.com/v3/user/webhooks/event/test   --header 'authorization: your_API_KEY_here'   --data '{"url": your_URL_here}' -v
```

Then (if you have Cloudwatcher Logs turned on for you'll notice logs coming in) you'll see items in Dynamo!
