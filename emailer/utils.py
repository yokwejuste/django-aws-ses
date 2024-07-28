import boto3
from botocore.exceptions import ClientError
from django.conf import settings

def send_ses_email(recipient, subject, body_text, body_html=None):
    client = boto3.client('ses', region_name=settings.AWS_REGION_NAME)

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [recipient],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': 'UTF-8',
                        'Data': body_text,
                    },
                    'Html': {
                        'Charset': 'UTF-8',
                        'Data': body_html,
                    } if body_html else {},
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': subject,
                },
            },
            Source=settings.DEFAULT_FROM_EMAIL,
        )
    except ClientError as e:
        print(f"An error occurred: {e.response['Error']['Message']}")
        return False
    else:
        print(f"Email sent! Message ID: {response['MessageId']}")
        return True
