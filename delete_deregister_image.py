import boto3


ec2 = boto3.client('ec2')

response = ec2.deregister_image(
    ImageId='ami-04fc23b297d4f502a'
)