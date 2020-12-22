import boto3
# Create SQS client
sqs = boto3.client('sqs')

#pro funkcnost je nutno mit v konfiguraku spravne i zonu

#zkopirovano z webu
queue_url = 'https://sqs.eu-central-1.amazonaws.com/ID/name'

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={

   
        "id": {
            'DataType': 'Number',
            'StringValue': "12"
        },

        "param1":
            {
                'DataType': 'String',
                'StringValue': "param-1"
            },
        "param2":
            {
                'DataType': 'String',
                'StringValue': "2"
            }


    },
    MessageBody=(
                'TODO?'


    )
)

print(response['MessageId'])
