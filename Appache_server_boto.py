
import boto3

def create_instance(client, ami_id, security_group_id,key_pair_name, user_data=none):
    response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType='t2.micro',
    KeyName=key_pair_name,
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        security_group_id,
    ]
    userData=user_data
)

ami_id = "ami-04fc23b297d4f502a"
key_pair_name = "ec2-learning"
security_group_id = "sg-07a2c2e8e73af4081"

user_data="""#!/bin/bash
    apt update -y
    apt-get install -y apache2
    systemctl start apache2
    systemctl enable apache2"""

ec2 = boto3.client('ec2')
create_instance(ec2, ami_id, security_group_id,key_pair_name, user_data)



