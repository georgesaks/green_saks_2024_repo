import boto3




internet_gateway_id = 'igw-0ab9f4977734f19d6'
vpc_id = 'vpc-071a07da153bd72e9'



ec2 = boto3.client('ec2')


ec2.detach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)

