import boto3


def get_sqs_resource():
    resource = boto3.resource('sqs', region_name='us-east-1',
                            aws_access_key_id='AKIAQLAIBKNOPOF6AUHT',
                            aws_secret_access_key='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')
    return resource


def get_sqs_client():
    client = boto3.client('sqs', region_name='us-east-1',
                            aws_access_key_id='AKIAQLAIBKNOPOF6AUHT',
                            aws_secret_access_key='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')
    return client


print(get_sqs_client())
