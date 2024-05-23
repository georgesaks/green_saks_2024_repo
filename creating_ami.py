import boto3




ec2 = boto3.client('ec2')

response = ec2.create_image(
    InstanceId='i-0f8903d50e55a64fd',
    Name='Demor'
)

print(response)