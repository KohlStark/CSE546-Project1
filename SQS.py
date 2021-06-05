import boto3

########## CREATING SQS CLIENT ##########
#client = boto3.resource('sqs', aws_access_key_id='AKIAQLAIBKNOJV3SM2N2', aws_secret_access_key='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', region_name='us-east-1')
#queue = client.get_queue_by_name(QueueName='response_queue_official.fifo')

########## SENDING MESSAGES ##########
'''
When sending messages, MessageGroupID REQUIRED for FIFO Queues.
If content-based deduplication is not enabled (done when settin up sqs), must include MessageDeduplicationId parameter.
If multiple messages are sent with the same deduplication id, they will be sent, but not delivered during the 5-minute window.
After 5 minutes, a message w same content/deduplicationId will be delivered.
'''
#once code is executed, message will be sent/received. Upon executing again immediately after, no output will be present.
#response1 = queue.send_message(MessageBody='Hello World!', MessageGroupId='messageGroup1', MessageDeduplicationId='1')
#response2 = queue.send_message(MessageBody='SQS Testing', MessageGroupId='messageGroup2', MessageDeduplicationId='2')

######### RECEIVING/DELETING MESSAGES ##########
# Print all messages in sqs (only does one at a time?)
#for message in queue.receive_messages():
#    print(message.body)
    # Let the queue know that the message is processed and remove it from the queue
    #message.delete()

#for message in queue.receive_messages():
    #print(message.body)

class SQS:
    def __init__(self, a_key, s_key, r, qn):
        """
        Constructor for saving SQS queue details
        """
        self.access_key = a_key
        self.secret_key = s_key
        self.region = r
        self.q_name = qn

        client = boto3.resource('sqs', aws_access_key_id=a_key, aws_secret_access_key=s_key, region_name=r)
        self.queue = client.get_queue_by_name(QueueName=qn)
