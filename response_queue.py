# This function gets the results from response queue
from typing import List, Any

import main

def sqs_client():
    client = main.get_sqs_client()
    response = client.receive_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/023639184220/response_queue_official',
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


# This function gets the number of messages currently in the queue
def get_res_queue_size():
    client = main.get_sqs_client()
    response = client.receive_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/023639184220/response_queue_official',
        AttributeNames=[
        ],
        MessageAttributeNames=[
            'string',
        ],
        MaxNumberOfMessages=10,
        VisibilityTimeout=10,
        WaitTimeSeconds=10,
    )

    flag = False
    size = 0
    return_statement = ''
    try:
        # Parsing json to get size:
        size = len(response['Messages'])
    except:
        flag = True
        return_statement = "Currently the size of the response queue is 0."

    if flag == False:
        return size
    else:
        return return_statement


# This function deletes a result from the response Queue
def delete_response_message():
    # Retrieving all messages in queue:
    client = main.get_sqs_client()
    response = client.receive_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/023639184220/response_queue_official',
        AttributeNames=[
        ],
        MessageAttributeNames=[
            'string'
        ],
        MaxNumberOfMessages=10,
        VisibilityTimeout=10,
        WaitTimeSeconds=10,
    )


    # Asking user which message they want to delete:
    message_index = input("Enter the index of the result you want to delete: ")
    message_index = int(message_index)

    try:
        message = response['Messages'][message_index]

        receipt_handle = message['ReceiptHandle']

        # Deleting message:
        client.delete_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/023639184220/request_queue_official',
            ReceiptHandle=receipt_handle
        )
        r = f' Deleted message at index: {message_index} '
        print(r)
    except:
        print("No results are currently in the request queue!")

    return ''


# This function deletes all the messages currently in the response queue
def delete_all_response_messages():
    # Retrieving all messages in queue:
    client = main.get_sqs_client()
    response = client.receive_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/023639184220/response_queue_official',
        AttributeNames=[
        ],
        MessageAttributeNames=[
            'string'
        ],
        MaxNumberOfMessages=10,
        VisibilityTimeout=10,
        WaitTimeSeconds=10,
    )

    try:
        length_queue = len(response['Messages'])
        for i in range(0, length_queue):
            message = response['Messages'][i]
            receipt_handle = message['ReceiptHandle']

            # Deleting message:
            client.delete_message(
                QueueUrl='https://sqs.us-east-1.amazonaws.com/023639184220/request_queue_official',
                ReceiptHandle=receipt_handle
            )

            print(f' Deleted result at index: {i} ')
    except:
        print("No results are currently in the request queue!")
    return ' '

    # This function sends an image to the Request Queue
def send_image_to_response_queue(my_string):
    #import main
    resource = main.get_sqs_resource()

    #file = 'test_0.JPEG'
    #converted_string = convert_image_to_string(file)

    # Sending image to request queue:
    queue = resource.get_queue_by_name(QueueName='response_queue_official')
    response = queue.send_message(MessageBody=str(my_string), MessageGroupId='Admin')
    print("Image sent to response queue")
    return response

'''
size = get_res_queue_size()
print(size)
delete_response_message()
size = get_res_queue_size()
print(size)

response = sqs_client()
first_result = get_first_result(response)
all_results = get_all_results(response)

#Converting string back to its jpeg file form
string = convert_string_to_jpeg(str(first_result['Message Body']))
print(string)
'''
#delete_all_response_messages()
#delete_response_message()