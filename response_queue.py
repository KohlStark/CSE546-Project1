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


# This function converts the string image to it's original format
def convert_string_to_jpeg(converted_string):
    import base64

    image_data = base64.b64decode(converted_string)
    image_filename = 'test_0_converted.JPEG'
    with open(image_filename, 'wb') as f:
        f.write(image_data)

    return image_filename


#response = sqs_client()
#first_result = get_first_result(response)
#all_results = get_all_results(response)

#Converting string back to its jpeg file form
#convert_string_to_jpeg(str(first_result['Message Body']))

def send_string_to_response_queue(output_string):
    #import main
    resource = main.get_sqs_resource()

    #file = 'test_2.JPEG'
    #converted_string = convert_image_to_string(file)

    # Sending image to request queue:
    queue = resource.get_queue_by_name(QueueName='response_queue_official.fifo')
    response = queue.send_message(MessageBody=str(output_string), MessageGroupId='Admin')
    print("Image sent to response queue")
    return response