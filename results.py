import response_queue
import main

client = main.get_sqs_resource()
queue = client.get_queue_by_name(QueueName='response_queue_official')

#infinite loop to continuously poll the response queue
while True:
    for msg in queue.receive_messages(MaxNumberOfMessages=10, MessageAttributeNames=['image_name']):

        # save body (the pair) and message attribute (the name)
        response_string = msg.body
        response_name = msg.message_attributes.get('image_name').get('StringValue')
        # print so it goes to stdout, which (i think) will route it to the response_queue_poller.stdout.on call
        # in test_app.js
        print(str(response_name) + ": " + str(response_string))

        # remove message from response queue after processing it
        msg.delete()
