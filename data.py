import boto3

print(“\nPrint the EC2 names from my AWS account\n”)
ec2client = boto3.client(‘ec2’)
response = ec2client.describe_instances()
for reservation in response[“Reservations”]:
for instance in reservation[“Instances”]:
# This will print will output the value of the Dictionary key ‘InstanceId’
print(instance[“InstanceId”])