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

print('Fetching Instance Information')
reservationsList=response['Reservations']
#print('\n reservationsList....')
#print(type(reservationsList))
#print(len(reservationsList))
for instanceListItemsIndex in range(len(reservationsList)):
    instanceList=(reservationsList[instanceListItemsIndex])['Instances']
    #print('\n instanceList....')
    #print(type(instanceList))
    #print(len(instanceList))
    for item in range(len(instanceList)):
        #print('Instance Information per Instance')
        print('Instance Id......'+(instanceList[item])['InstanceId'])        
        print('Key name......'+(instanceList[item])['KeyName'])
        tagsList=(instanceList[item])['Tags']
        #print(tagsList)
        #print(type(tagsList))
        #print('Iterating Tags')
        for keyvaluePair in range(len(tagsList)):
            print('Tags :Name:'+(tagsList[keyvaluePair])['Key']+'   Value:'+((tagsList[keyvaluePair])['Value']))        
        
       
