import boto3



route_table_id = "rtb-0dcb7eea46152146e"

ec2 = boto3.client('ec2')


ec2.delete_route_table(
    RouteTableId=route_table_id,
)

