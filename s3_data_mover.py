import boto3

images_path = "/Users/KohlStark/Documents/CSE546/CSE546-Project1/imagenet-100/"

download_path = "/Users/KohlStark/Documents/CSE546/CSE546-Project1"

client = boto3.client('s3', region_name='us-east-2')

def uploadPicture(picPath, bucketName, s3Name):
    client.upload_file(picPath, bucketName, s3Name)
    
def downloadPicture(bucketName, s3Name, picPath):
    client.download_file(bucketName, s3Name, picPath)

#uploadPicture(images_path + 'test_0.JPEG', 'cse-546-picture-files', 'test_0.JPEG')
downloadPicture('cse-546-picture-files', 'test_0.JPEG', download_path + 'test_0.JPEG')