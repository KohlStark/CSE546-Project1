import boto3

# This function converts a jpeg image to a string
def convert_image_to_string(file):
    import base64

    with open(file, "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())

    with open('encode.bin', "wb") as file:
        file.write(converted_string)

    return converted_string


# This function converts the string image to it's original format
def convert_image_to_jpeg(converted_string):
    import base64

    #print(converted_string)
    image_data = base64.b64decode(converted_string)
    image_filename = 'test_0_converted.JPEG'
    with open(image_filename, 'wb') as f:
        f.write(image_data)

    return image_filename


# This function classifies the image:
def classify_image():

    result = "{'test': 'bathtub'}"
    return result


# This function gets the s3 resources:
def get_sqs_resource():
    resource = boto3.resource('sqs', region_name='us-east-1',
                              aws_access_key_id='AKIAQLAIBKNOC25ZCNQS',
                              aws_secret_access_key='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')
    return resource


# This function sends the image classification result to the response queue
def send_result_response_queue(result):
    resource = get_sqs_resource()

    # Sending results to request queue:
    queue = resource.get_queue_by_name(QueueName='response_queue_official.fifo')
    response = queue.send_message(MessageBody=result, MessageGroupId='Admin')
    return response


# This function sends the result to the output bucket in S3 to be stored
def send_result_S3(result):
    # Putting results into a text file:
    write_file = result + ".txt"
    f = open(write_file, "w+")
    f.write(result)

    # Sending text file to S3:
    s3 = boto3.client('s3', region_name='us-east-1',
                      aws_access_key_id='AKIAQLAIBKNOC25ZCNQS',
                      aws_secret_access_key='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')

    with open(write_file, 'rb') as f:
        s3.upload_fileobj(f, 'output-bucket-cse-546', write_file)
    return


#Converting file to sttring and vice versa:
#file = 'test_2.JPEG'
#converted_string = convert_image_to_string(file)

#print(converted_string)
#image_filename = convert_image_to_jpeg(converted_string)


# Sending results to response queue and S3 at the same time:

#image_filename = convert_image_to_jpeg(string)

#result = classify_image()
#send_result_response_queue(result)
#send_result_S3(result)

