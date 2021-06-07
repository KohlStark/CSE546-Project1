import image_classification
import request_queue
import response_queue
import ec2_instance_manager
import convert_image
#from ec2_metadata import ec2_metadata


#this_instance_id = ec2_metadata.instance_id
#print("Started instance (worker):", this_instance_id)

print("Getting string image from request queue")
request = request_queue.sqs_client()
result = request_queue.get_first_result(request)
print("Got image from request queue", result)
image_name_from_message = result['MessageAttributes']['image_name']['StringValue']
request_string = result['Message Body']
#sliced_string = request_string[1:]
#print(sliced_string)

string_image = result['Message Body']
image_filename = convert_image.convert_image_to_jpeg(request_string)

classification_result = image_classification.image_classification(image_filename)

return_string = image_name_from_message + ", " + classification_result
#print(return_string)

response_queue.send_image_to_response_queue(return_string)









#result = image_classification.image_classification()
