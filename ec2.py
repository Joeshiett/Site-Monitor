import boto3
import logging
from botocore.exceptions import ClientError

def get_running_instance():
    ec2_client = boto3.client('ec2', region_name='eu-west-1')
    reservations = ec2_client.describe_instances(Filters=[{
        "Name": "instance-state-name",
        "Values": ["running"],
    }]).get("Reservations")

    try:
        for reservation in reservations:
            for instance in reservation["Instances"]:
                instance_id = instance["InstanceId"]
                instance_type = instance["InstanceType"]
                public_ip = instance["PublicIpAddress"]
                private_ip = instance["PrivateIpAddress"]
                print(f'''
                Instance Id:{instance_id}
                Instance Type:{instance_type}
                Public Ip:{public_ip}
                Private Ip:{private_ip}
                ''')
    except ClientError as e:
        logging.error(e)
        return False
    
get_running_instance()