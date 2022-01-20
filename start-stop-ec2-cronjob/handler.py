import boto3

ec2 = boto3.client('ec2')

def start_ec2(event,context):
    # print(event)
    ec2_instances = get_all_ec2_ids()
    response = ec2.start_instances(
        InstanceIds = ec2_instances
    )
    # print(response)
    return response

def stop_ec2(event,context):
    ec2_instances = get_all_ec2_ids()
    response = ec2.stop_instances(
        InstanceIds = ec2_instances
    )
    # print(response)
    return response

def get_all_ec2_ids():
    response = ec2.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] != 'terminated':
                instances.append(instance['InstanceId'])

    # print(instances)
    return instances
