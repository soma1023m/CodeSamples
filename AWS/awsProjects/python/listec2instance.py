import sys
import boto3
delete_mode =False
print('\n Coonecting to aws......')
ec2_client = boto3.client('ec2')

print('\n Fetching Ec2 instances begin......')
response = ec2_client.describe_instances(
    Filters=[
        {
        'Name': 'instance-state-name',
        'Values': [
            'running',
        ]
        },
    ]
)
print('\n Fetching Ec2 instances end......')
print(response)