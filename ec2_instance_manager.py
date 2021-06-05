import boto3
import os

def create_key_pair():
    print("Creating key pair")
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    key_pair = ec2_client.create_key_pair(KeyName="my_ec2_key")

    private_key = key_pair["KeyMaterial"]

    # write private key to file with 400 permissions
    
    
    private_key_file=open("my_ec2_key","w")
    private_key_file.write(private_key)
    private_key_file.close

    print("Finished creating key pair")

def get_public_ip(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get("Reservations")

    for reservation in reservations:
        for instance in reservation['Instances']:
            print(instance.get("PublicIpAddress"))

def create_instance():
    print("Creating new instance")
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    instances = ec2_client.run_instances(
        ImageId="ami-0ee8cf7b8a34448a6",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="ec2-key-pair"
    )
    print("Done creating instance")
    print("Instance id:", instances["Instances"][0]["InstanceId"])

def bulk_create_instances(num):
    print("Starting bulk create of", num, "instances")
    for i in range(num):   
        create_instance() 


def stop_instance(instance_id):
    print("Stopping instance:", instance_id)
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    response = ec2_client.stop_instances(InstanceIds=[instance_id])
    print(response)


def terminate_instance(instance_id):
    print("Terminating instance:", instance_id)
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    response = ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(response)

def stop_and_terminate(instance_id):
    stop_instance(instance_id)
    terminate_instance(instance_id)

def bulk_stop_and_terminate(instance_ids):
    instance_ids.remove("i-0a4039b7c8b46a8df")
    print("Deleting these instances", instance_ids)
    for i in instance_ids:
        stop_instance(i)
        terminate_instance(i)




def get_running_instances():
    instance_list = []
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    reservations = ec2_client.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"],
        }
    ]).get("Reservations")

    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            public_ip = instance["PublicIpAddress"]
            private_ip = instance["PrivateIpAddress"]
            print("Here are your instances:")
            print(f"{instance_id}, {instance_type}, {public_ip}, {private_ip}")
            instance_list.append(instance_id)
    return instance_list
            

#create_key_pair()
#create_instance()
#get_public_ip("i-096b2fa8bbc536c4b")


#stop_instance("i-096b2fa8bbc536c4b")
#terminate_instance("i-096b2fa8bbc536c4b")

#bulk_create_instances(5)
instance_list = get_running_instances()
#bulk_stop_and_terminate(instance_list)