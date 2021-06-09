import image_classification
import request_queue
import response_queue
import ec2_instance_manager
import convert_image
import requests

#production = sys.argv[1]

file1 = open("Begin.txt", "w")
write_string = "begin"
file1.write(write_string)



response = requests.get('http://169.254.169.254/latest/meta-data/instance-id')
instance_id = response.text
print("Started instance (worker):", instance_id)



queue_size = request_queue.get_req_queue_size()
print("Queue size:", queue_size)

while queue_size > 0:
    print("Getting string image from request queue")
    request = request_queue.sqs_client()
    result = request_queue.get_first_result(request)

    print("Got image from request queue")
    image_name_from_message = result['MessageAttributes']['image_name']['StringValue']
    request_string = result['Message Body']

    print("Removing image from request queue")
    request_queue.delete_request_message()

    image_filename = convert_image.convert_image_to_jpeg(request_string)
    print("Finished converting image")

    classification_result = image_classification.image_classification(image_filename)

    return_string = image_name_from_message + ", " + classification_result
    #print(return_string)

    # Send classified image to response queue 
    response_queue.send_image_to_response_queue(return_string)

    # Send result to S3

    convert_image.send_result_S3(return_string)

    # Get queue size
    queue_size = request_queue.get_req_queue_size()
    print("Result sent to S3")
    print("New queue size", queue_size)

# if production != 'test':
#     print("Stopping instance:", instance_id)
#     ec2_instance_manager.stop_instance(instance_id)


file1.write("End")
file1.close()



