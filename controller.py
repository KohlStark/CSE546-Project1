from numpy.lib.function_base import diff
import ec2_instance_manager
import boto3
import request_queue
import time


def auto_scale_instances():
    queue_length = request_queue.get_req_queue_size()

    # all_instances = ec2_instance_manager.get_all_instances()
    # print("All instances:", all_instances)
    # all_instances_size = len(all_instances)
    #queue_length = 1
    print("Request queue length:", queue_length)

    if queue_length == 0:
        print("Queue is empty, shutting down all instances (downscaling)")
        ec2_instance_manager.bulk_stop_instances()
        return

    else:
        running_instances = ec2_instance_manager.get_running_instances()
        running_instances_size = len(running_instances)
        print("Running instances:", running_instances)
        
        
        if running_instances_size < queue_length:
            stopped_instances = ec2_instance_manager.get_stopped_instances()
            num_of_available_instaces = len(stopped_instances)
            difference = min(queue_length, num_of_available_instaces)

            if difference == 0:
                return # have instances = to queue size
            else:
                del_num = num_of_available_instaces - queue_length
                if del_num > 0:
                    temp_list = stopped_instances
                    del temp_list[:del_num]
                    ec2_instance_manager.bulk_start_instances(temp_list)

    
                
        #elif running_instances_size == queue_length:
        else:
            return







            
            


while True:
    auto_scale_instances()
    time.sleep(30)