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
print("Got image from request queue")
request_string = result['Message Body']
sliced_string = request_string[1:]
#print(sliced_string)

string_image = result['Message Body']
image_filename = convert_image.convert_image_to_jpeg(sliced_string)

classification_result = image_classification.image_classification(image_filename)





#result = image_classification.image_classification()
