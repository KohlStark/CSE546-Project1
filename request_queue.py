# Make modifications to the request queue here:
import main


# This function gets the number of messages currently in the queue
def get_req_queue_size():
    
    client = main.get_sqs_client()
    response = client.receive_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/023639184220/request_queue_official.fifo',
        AttributeNames=[
        ],
        MessageAttributeNames=[
            'string',
        ],
        MaxNumberOfMessages=10,
        VisibilityTimeout=10,
        WaitTimeSeconds=10,
    )

    # Parsing json to get size:
    size = len(response['Messages'])
    return size


# This function converts a jpeg image to a string
def convert_image_to_string(file):
    import base64
    with open(file, "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())

    with open('encode.bin', "wb") as file:
        file.write(converted_string)

    return converted_string


# This function sends an image to the Request Queue
def send_image_to_request_queue():
    #import main
    resource = main.get_sqs_resource()

    file = 'test_2.JPEG'
    converted_string = convert_image_to_string(file)

    # Sending image to request queue:
    queue = resource.get_queue_by_name(QueueName='request_queue_official.fifo')
    response = queue.send_message(MessageBody=str(converted_string), MessageGroupId='Admin')
    return response

# This function deletes an image from the request Queue
def delete_request_message():
    # Retrieving all messages in queue:
    client = main.get_sqs_client()
    response = client.receive_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/023639184220/request_queue_official.fifo',
        AttributeNames=[
        ],
        MessageAttributeNames=[
            'string'
        ],
        MaxNumberOfMessages=10,
        VisibilityTimeout=10,
        WaitTimeSeconds=10,
    )
    print("PRINTING: ")

    # Asking user which message they want to delete:
    message_index = input("Enter the index of the message you want to delete: ")
    message_index = int(message_index)
    message = response['Messages'][message_index]

    receipt_handle = message['ReceiptHandle']

    # Deleting message:
    client.delete_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/023639184220/request_queue_official.fifo',
        ReceiptHandle=receipt_handle
    )

    r = f' Deleted message at index: {message_index} '
    return r

def sqs_client():
    client = main.get_sqs_client()
    request = client.receive_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/023639184220/request_queue_official.fifo',
        AttributeNames=[
        ],
        MessageAttributeNames=[
            'string',
        ],
        MaxNumberOfMessages=10,
        VisibilityTimeout=10,
        WaitTimeSeconds=10,
    )

    return request

# This function gets the first result in the response queue:
def get_first_result(request):
    first_result = {}
    first_result['Message ID'] = request['Messages'][1]['MessageId']
    first_result['Message Body'] = request['Messages'][1]['Body']
    return first_result


# This function gets all the results in the response queue:
def get_all_results(request):
    all_results = {}

    messages_length = len(request['Messages'])

    for i in range(0, messages_length):
        all_results[f'Message {i} ID '] = request['Messages'][i]['MessageId']
        all_results[f'Message {i} Body'] = request['Messages'][i]['Body']

    return all_results


#request = sqs_client()
#first_result = get_first_result(request)
#print(first_result)

#all_results = get_all_results(request)
#print(all_results)

#send_image_to_request_queue()