import response_queue
import sys
import main
import time

client = main.get_sqs_resource()
queue = client.get_queue_by_name(QueueName='response_queue_official')

#infinite loop to continuously poll the response queue
while True:
    for msg in queue.receive_messages(MaxNumberOfMessages=10):
        # save body (the pair) and message attribute (the name)
        response_string = msg.body
        response_name = str(msg.body).split(", ")
        #print("Got message, writing to sys.stdout")
        #print("Message name: " + response_name[0])
        #print("Message body: " + response_string)
        # print so it goes to stdout, which (i think) will route it to the response_queue_poller.stdout.on call
        # in test_app.js
        print(str(response_name[0]) + ": " + str(response_string))
        sys.stdout.flush()

        #print("Removing message")
        # remove message from response queue after processing it
        msg.delete()
    #time.sleep(5)
