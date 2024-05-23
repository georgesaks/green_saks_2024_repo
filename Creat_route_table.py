import boto3


vpc_id = 'vpc-071a07da153bd72e9'

ec2 = boto3.client('ec2')


routeTable = ec2.create_route_table(VpcId=vpc_id)

print(routeTable["RouteTable"]["RouteTableId"])