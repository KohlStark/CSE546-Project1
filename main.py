import boto3


def get_sqs_resource():
    resource = boto3.resource('sqs', region_name='us-east-1',
                            aws_access_key_id='AKIAQLAIBKNOC25ZCNQS',
                            aws_secret_access_key='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')
    return resource


def get_sqs_client():
    client = boto3.client('sqs', region_name='us-east-1',
                            aws_access_key_id='AKIAQLAIBKNOC25ZCNQS',
                            aws_secret_access_key='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')
    return client


print(get_sqs_client())
