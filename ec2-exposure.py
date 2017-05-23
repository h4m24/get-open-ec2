import boto3
from prettytable import PrettyTable

InstanceSecurityGroupList =[]
client = boto3.client('ec2')

report = PrettyTable(['Name', 'publicDNS', 'instanceID'])

for Ec2Instance in client.describe_instances()['Reservations']:


    InstanceSecurityGroupList.clear()


    if Ec2Instance['Instances'][0]['PublicDnsName'] != '':

        for SecurityGroupId in Ec2Instance['Instances'][0]['SecurityGroups']:
            InstanceSecurityGroupList.append(SecurityGroupId['GroupId'])

        for Cidrs in client.describe_security_groups(GroupIds=InstanceSecurityGroupList)['SecurityGroups'][0]['IpPermissions'][0]['IpRanges']:
            if Cidrs['CidrIp'] == '0.0.0.0/0':

                for TagDocument in Ec2Instance['Instances'][0]['Tags']:
                    if TagDocument['Key'] == 'Name':
                        Ec2Name = TagDocument['Value']

                report.add_row([Ec2Name, Ec2Instance['Instances'][0]['PublicDnsName'],Ec2Instance['Instances'][0]['InstanceId']])

                continue

print(" following instances with 0.0.0.0/0 in security group setup:")
print(report)
