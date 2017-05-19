import boto3

InstanceSecurityGroupList =[]
client = boto3.client('ec2')



for Ec2Instance in client.describe_instances()['Reservations']:


    InstanceSecurityGroupList.clear()


    if Ec2Instance['Instances'][0]['PublicDnsName'] != '':

        for SecurityGroupId in Ec2Instance['Instances'][0]['SecurityGroups']:
            InstanceSecurityGroupList.append(SecurityGroupId['GroupId'])

        for Cidrs in client.describe_security_groups(GroupIds=InstanceSecurityGroupList)['SecurityGroups'][0]['IpPermissions'][0]['IpRanges']:
            if Cidrs['CidrIp'] == '0.0.0.0/0':

                print("Instance info:")
                print(InstanceSecurityGroupList)
                print(Ec2Instance['Instances'][0]['PublicDnsName'])
                print(Ec2Instance['Instances'][0]['InstanceId'])
                print(Ec2Instance['Instances'][0]['Tags'])
                for Cidrs in client.describe_security_groups(GroupIds=InstanceSecurityGroupList)['SecurityGroups'][0]['IpPermissions'][0]['IpRanges']:
                    print(Cidrs['CidrIp'])
                print("\n")
                print("\n")
                continue
