import boto3
import logging
import logging.config
from dotenv import dotenv_values
from botocore.exceptions import ClientError

# Note: initialize logging module
__env__ = dotenv_values(".env")
__author_name__ = __env__.get("author")
__logger_tag__=__env__.get('logger_tag')

logging.config.fileConfig(fname='log.conf')
logger= logging.getLogger(f'{__logger_tag__}')

# Note: initialize creating fuctuon
def create_security_group(input_ec2: boto3, input_sg_name: str, input_sg_descrbe: str, input_vpc_id: str):
    """Create the AWS Security Group by Boto3 EC2.

    Args:
        input_ec2 (boto3): _description_
        input_sg_name (str): _description_
        input_sg_descrbe (str): _description_
        input_vpc_id (str): _description_
    """    
    try:
        response_checking = input_ec2.describe_security_groups(Filters=[
            {'Name': f'tag:Name', 'Values': [input_sg_name]}
            ])
        
        if response_checking['SecurityGroups']:
            security_group_params = {
                'GroupName': input_sg_name,     
                'Description': input_sg_descrbe, 
                'VpcId': input_vpc_id,            
            }
            response_createing = input_ec2.create_security_group(**security_group_params)
            security_group_id = response_createing['GroupId']
            tag_params = {
                'Resources': [security_group_id],  
                'Tags': [
                    {'Key': 'Name', 'Value': input_sg_name},
                    {'Key': 'Author', 'Value': __author_name__}
                ]
            }
            ec2.create_tags(**tag_params)
            logger.info(f"Security Group Name: '{input_sg_name}({security_group_id})' Created!")
        else:
            logger.info(f"The security group '{input_sg_name}' already exists for VPC '{input_vpc_id}'")

    except Exception as err:
        logger.info(f"Security Group Name: '{input_sg_name}' Create Failed!")
        logger.info(f"Unexpected: {err}, {type(err)}")    

# Note: initialize deleting fuctuon
def delete_security_group(input_ec2: boto3, input_sg_name: str):
    """Delete the Security Group by Boto3 EC2.

    Args:
        ec2 (boto3): _description_
        input_sg_name (str): _description_
    """   

    try:
        response_checking = input_ec2.describe_security_groups(Filters=[
            {'Name': f'tag:Name', 'Values': [input_sg_name]}
            ])
        if response_checking['SecurityGroups']:
            security_group = response_checking['SecurityGroups'][0]
            security_group_id = security_group['GroupId']
            input_ec2.delete_security_group(GroupId=security_group_id)
            logger.info(f"Security Group Name: '{input_sg_name}({security_group_id})' Deleted!")
        else:
            logger.info(f"No security groups found with the tag '{'Name'}={input_sg_name}'.")

    except Exception as err:
        logger.info(f"Security Group Name: '{input_sg_name}' Delete Failed!")
        logger.info(f"Unexpected: {err}, {type(err)}")
    
# Note: the application start
vpc_id = __env__.get('vpc_id')
sg_name = __env__.get('sg_name')
sg_describe = __env__.get('sg_describe')
action = __env__.get('appliction_action')
ec2 = boto3.client('ec2')

try:
    if (action=='create'):
        create_security_group(ec2, sg_name, sg_describe, vpc_id)
    elif (action=='delete'):
        delete_security_group(ec2, sg_name)
    else:
        logger.info(f"The action '{action}' is not supported.")
except Exception as err:
    logger.info(f"Unexpected: {err}, {type(err)}")