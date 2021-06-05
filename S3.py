import boto3
from SQS import SQS

class S3:
    def __init__(self, bn):
        """
        Constructor for saving S3 bucket details
        """
        self.bucket_name = bn

        s3 = boto3.resource('s3')
        self.bucket = s3.Bucket(bn)

    def get_items(self):
        """
        Reads all items from the given S3 bucket

        @param: bucket_name: str        Name of bucket to be read from
        @return: items:      list       Python list of the message bodies of all items
        """

        #read bucket iteratively, appending to items list
        items = []
        for obj in self.bucket.objects.all():
            key = obj.key
            body = obj.get()['Body'].read()
            #print(key)
            items.append(body)

        return items

    #get_items('cse-546-picture-files')

    def put_response(self, msg, sqs_obj):
        """
        Given a message from the S3 bucket, will send the message to the respective SQS Queue

        @param: msg:        str      Message to be sent
                q_name:     str      Name of queue to send message to
                access_key: str      AWS access key
                secret_key: str      Private AWS access key
                region:     str      Server region

        @return: boolean: True if successful, False otherwise
        """

        try:
            #send message to queue
            response_q = sqs_obj.queue.send_message(MessageBody=str(msg), MessageGroupId='user1')
            return True
        except Exception as e:
            print(e)
            return False

#buckets = S3('cse-546-picture-files')
#sqs_test = SQS('AKIAQLAIBKNOJV3SM2N2', 'Tuem2P33Fc++Hj4jGP2KirHvmQrXEUW7y6WiaTzq', 'us-east-1', 'response_queue_official.fifo')
#message = buckets.get_items()[0]
#print(buckets.put_response(message, sqs_test))
