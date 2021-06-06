import ec2_instance_manager
import boto3
import request_queue


def auto_scale_instances():
    queue_length = request_queue.get_req_queue_size()
    print("Request queue length:", queue_length)


auto_scale_instances()