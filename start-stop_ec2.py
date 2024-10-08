import json
import boto3

region = 'ap-south-1'
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    instances = event["instances"].split(',')
    action = event["action"]
    
    if action == 'Start':
        print("STARTing your instances: " + str(instances))
        ec2.start_instances(InstanceIds=instances)
        response = "Successfully started instances: " + str(instances)
    elif action == 'Stop':
        print("STOPping your instances: " + str(instances))
        ec2.stop_instances(InstanceIds=instances)
        response = "Successfully stopped instances: " + str(instances)
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }