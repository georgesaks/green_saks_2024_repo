import boto3


internet_gateway_id = 'igw-0ab9f4977734f19d6'



ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)

