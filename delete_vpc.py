import boto3

vpc_id = 'vpc-071a07da153bd72e9'


ec2 = boto3.client('ec2')


ec2.delete_vpc(
    VpcId=vpc_id,
)

