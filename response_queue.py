# This function gets the results from response queue
from typing import List, Any

import main

def sqs_client():
    client = main.get_sqs_client()
    response = client.receive_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/023639184220/response_queue_official.fifo',
        AttributeNames=[
        ],
        MessageAttributeNames=[
            'string',
        ],
        MaxNumberOfMessages=10,
        VisibilityTimeout=10,
        WaitTimeSeconds=10,
    )

    return response

# This function gets the first result in the response queue:
def get_first_result(response):
    first_result = {}
    first_result['Message ID'] = response['Messages'][0]['MessageId']
    first_result['Message Body'] = response['Messages'][0]['Body']
    return first_result


# This function gets all the results in the response queue:
def get_all_results(response):
    all_results = {}

    messages_length = len(response['Messages'])

    for i in range(0, messages_length):
        all_results[f'Message {i} ID '] = response['Messages'][i]['MessageId']
        all_results[f'Message {i} Body'] = response['Messages'][i]['Body']

    return all_results


response = sqs_client()
first_result = get_first_result(response)
print(first_result)
all_results = get_all_results(response)
print(all_results)