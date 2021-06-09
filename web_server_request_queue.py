# Make modifications to the request queue here:
import main
import sys
import base64

images_path = "/home/ubuntu/upload_images/"
#images_path = "/Users/KohlStark/Documents/CSE546/CSE546-Project1/"
firstarg=sys.argv[1]

# This function converts a jpeg image to a string
def convert_image_to_string(file):
    
    with open(file, "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())

    with open('encode.bin', "wb") as file:
        file.write(converted_string)

    return converted_string


# This function sends an image to the Request Queue
def send_image_to_request_queue(file):
    #import main
    resource = main.get_sqs_resource()

    #file = 'test_2.JPEG'
    converted_string = convert_image_to_string(file)

    # Sending image to request queue:
    queue = resource.get_queue_by_name(QueueName='request_queue_official')
    response = queue.send_message(MessageBody=str(converted_string),MessageAttributes = {
        'image_name': {
            "StringValue": firstarg,
            "DataType": "String"

        }
    })
    print("Image:", file, "sent to queue as string")
    return response



def sqs_client():
    client = main.get_sqs_client()
    request = client.receive_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/023639184220/request_queue_official',
        AttributeNames=[
        ],
        MessageAttributeNames=[
            'All',
        ],
        MaxNumberOfMessages=10,
        VisibilityTimeout=10,
        WaitTimeSeconds=10,
    )

    return request

# This function gets the first result in the response queue:
def get_first_result(request):
    first_result = {}
    first_result['Message ID'] = request['Messages'][0]['MessageId']
    first_result['Message Body'] = request['Messages'][0]['Body']
    return first_result

send_image_to_request_queue(images_path + firstarg)

#request = sqs_client()
#print(request)
