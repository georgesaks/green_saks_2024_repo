import boto3


route_table_id = "rtb-0dcb7eea46152146e"
internet_gateway_id = "igw-0ab9f4977734f19d6"

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)

