import boto3
import sys

images_path = "/home/ubuntu/upload_images/"
firstarg=sys.argv[1]
client = boto3.client('s3', region_name='us-east-1')

def uploadPicture(picPath, bucketName, s3Name):
    client.upload_file(picPath, bucketName, s3Name)
    print("Success uploading", picPath, " to S3")
    
def downloadPicture(bucketName, s3Name, picPath):
    client.download_file(bucketName, s3Name, picPath)

uploadPicture(images_path + firstarg, 'cse-546-picture-files', firstarg)