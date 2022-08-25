import boto3

#Define variables
AWS_REGION = "eu-central-1"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
instances = EC2_RESOURCE.instances.all()
volumes = EC2_RESOURCE.volumes.all()

#Define a function to sort volume
def my_sort_key(volume):
  return volume.size

#iterate through the returned list of instances
for instance in instances:
#iterate through the returned list ordered by volume size    
 for volume in sorted(volumes, key=my_sort_key):  
#iterate through the tags from the returned list of instance tags    
  for tags in instance.tags:  
    print(f'EC2 instance id: {instance.id}')
    print(f'Instance type: {instance.instance_type}')    
    print(f'Instance state: {instance.state["Name"]}')
    print(f'Instance name: {tags["Value"]}')    
    print(f'Private IPv4 address: {instance.private_ip_address}')    
    print(f'Public IPv4 address: {instance.public_ip_address}')
    print(f'Volume {volume.size} GiB')