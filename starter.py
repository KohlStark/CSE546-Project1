import main

ec2 = main.get_ec2_client()
response = ec2.start_instances(InstanceIds=["i-0c6fe4c893fc48b1d"], DryRun=False)
print(response)