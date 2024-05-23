import boto3


ec2 = boto3.client

response = ec2.delete_security_group(
    GroupId='sg-07a2c2e8e73af4081',
)

print(response)