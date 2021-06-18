import sys
import main
import time

client = main.get_sqs_resource()
queue = client.get_queue_by_name(QueueName='response_queue_official')

firstarg = sys.argv[1]

def printOutputs(num_requests):
    #infinite loop to continuously poll the response queue
    requests_met = 0
    outputs = ""
    while True:
        if requests_met == num_requests:
            print(outputs)
            sys.stdout.flush()
            return
        else:
            for msg in queue.receive_messages(MaxNumberOfMessages=10):
                # save body (the pair) and message attribute (the name)
                response_string = msg.body
                response_name = str(msg.body).split(", ")
                # build output string
                outputs += ("(" + str(response_name[0][:-5]) + ", " + str(response_name[1]) + ")\n")

                # remove message from response queue after processing it
                msg.delete()

                #update requests_met
                requests_met += 1
                time.sleep(1)
            #time.sleep(5)

printOutputs(firstarg)
