import boto3
import logging
import logging.config
from dotenv import dotenv_values

# initialize logging module
env = dotenv_values(".env")

logger_tag=env.get('logger_tag')
logging.config.fileConfig(fname='log.conf')
logger = logging.getLogger(f'{logger_tag}')

def create_security_group(input_ec2: boto3, input_sg_name: str, input_sg_descrbe: str, input_vpc_id: str):
    """Create the AWS Security Group by Boto3 EC2.

    Args:
        input_ec2 (boto3): _description_
        input_sg_name (str): _description_
        input_sg_descrbe (str): _description_
        input_vpc_id (str): _description_
    """    

    try:
        # security_group_params = {
        #     'GroupName': input_sg_name,     
        #     'Description': input_sg_descrbe, 
        #     'VpcId': input_vpc_id,            
        # }
        # response = input_ec2.create_security_group(**security_group_params)
        # security_group_id = response['GroupId']

        # tag_params = {
        #     'Resources': [security_group_id],  
        #     'Tags': [
        #         {'Key': 'Name', 'Value': input_sg_name} 
        #     ]
        # }
        # ec2.create_tags(**tag_params)

        # Mock Security Group ID
        output_sg_id = 'mock_security_group_id'
        logger.info(f"Security Group Name: '{input_sg_name}({output_sg_id})' Created!")
    except Exception as err:
        logger.info(f"Security Group Name: '{input_sg_name}' Create Failed!")
        logger.info(f"Unexpected: {err}, {type(err)}")    

def delete_security_group(input_ec2: boto3, input_sg_name: str):
    """Delete the Security Group by Boto3 EC2.

    Args:
        ec2 (boto3): _description_
        input_sg_name (str): _description_
    """   

    try:
        # response = input_ec2.describe_security_groups(Filters=[
        #     {'Name': f'tag:Name', 'Values': [input_sg_name]}
        #     ])
        # if response['SecurityGroups']:
        #     security_group = response['SecurityGroups'][0]
        #     security_group_id = security_group['GroupId']
        #     input_ec2.delete_security_group(GroupId=security_group_id)
        #     logger.info(f"Security Group Name: '{input_sg_name}({output_sg_id})' Deleted!")
        # else:
        #     logger.info(f"No security groups found with the tag '{'Name'}={input_sg_name}'.")

        # Mock Security Group ID
        output_sg_id = 'mock_security_group_id'    
        logger.info(f"Security Group Name: '{input_sg_name}({output_sg_id})' Deleted!")
    except Exception as err:
        logger.info(f"Security Group Name: '{input_sg_name}' Delete Failed!")
        logger.info(f"Unexpected: {err}, {type(err)}")
    

vpc_id = env.get('vpc_id')
sg_name = env.get('sg_name')
sg_describe = env.get('sg_describe')
ec2 = 'mock boto3 client object'
# ec2 = boto3.client('ec2')

try:
    create_security_group(ec2, sg_name, sg_describe, vpc_id)
    delete_security_group(ec2, sg_name)
except Exception as err:
    logger.info(f"Unexpected: {err}, {type(err)}")