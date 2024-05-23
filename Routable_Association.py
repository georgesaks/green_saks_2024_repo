import boto3


route_table = 'rtb-0dcb7eea46152146e'
subnet_id = 'subnet-08649b7fa619f4145'

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table,
    SubnetId=subnet_id,
)

print(association["AssociationId"])