CSE 546 Project 1: Image Classification Auto-scaling Architecture

Group Members:
  Kohl Stark (kgstark1@asu.edu)
  Ian Bolton (ipbolton@asu.edu)
  Samuel Steinberg (ssteinb5@asu.edu)

Web Tier Public IP:
  Determined at program execution. Please refer to the project PDF for execution details.

SQS Names:
  request_queue_official: The SQS queue which takes in the images
  response_queue_official: The SQS queue which returns the output pair

S3 Names:
  cse-546-picture-files: S3 input storage
  output-bucket-cse-546: S3 output storage
