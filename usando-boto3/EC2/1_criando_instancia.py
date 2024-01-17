import boto3

sessao = boto3.Session(profile_name="python-lambda-ricardo")

cliente_ec2 = sessao.client('ec2')

# variaveis uteis
nome_chave = 'lambda-tarik.pem'
vpc_id = 'vpc-0d87f3e58392ef4a8'  # vpc usado para cloudtreinamentos
subnet_id = 'subnet-0b4008fd38cfdc22b'  # subnet publica_01
ami_id = 'ami-0c7217cdde317cfec'  # ubuntu 22.04 64b_x86

# criando novo SG dentro de uma VPC específica via codigo, usando tratamento de erro pra nao ficar apitando erro caso sg ja exista:
try:
    resposta_sg = cliente_ec2.create_security_group(
        Description='SG lambda-tarik',
        GroupName='sg_lambda_web',
        VpcId=vpc_id
    )
    sg_id = resposta_sg['GroupId']

    # Definindo regras de entrada para o SG:
    resposta_ingress = cliente_ec2.authorize_security_group_ingress(
        GroupId=sg_id,
        IpPermissions=[
            {
                'FromPort': 22,
                'ToPort': 22,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/0',
                        'Description': 'Acesso SSH'
                    }
                ]
            },
            {
                'FromPort': 80,
                'ToPort': 80,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/0',
                        'Description': 'Acesso HTTP'
                    }
                ]
            }
        ]
    )

except Exception as erro:
    print('sg_lambda_web já existe!')
    resposta_grupos = cliente_ec2.describe_security_groups(
        Filters = [
    {
        'Name': 'vpc-id',
        'Values': [vpc_id]
    },
    {
        'Name': 'group-name',
        'Values': ['sg_lambda_web']
    }
    ]
    )
    sg_id = resposta_grupos['SecurityGroups'][0]['GroupId']
# fim da definição do SG

# carregando user data do wordpress na EC2 (pasta ec2):
arquivo_user_data = open('ec2/wp_user_data.sh', 'r')
user_data = arquivo_user_data.read()

# iniciando ec2 e sua longa lista de parametros:
resposta_ec2 = cliente_ec2.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sda1',
            'Ebs': {
                'VolumeSize': 8,
                'DeleteOnTermination': True,
                'VolumeType': 'gp2',
                'Encrypted': False
            }
        }
    ],
    UserData=user_data,
    ImageId=ami_id,
    MaxCount=1,
    MinCount=1,
    InstanceType='t2.micro',
    KeyName=nome_chave,
    Monitoring={'Enabled': False},
    SecurityGroupIds=[sg_id],
    SubnetId=subnet_id,
    InstanceInitiatedShutdownBehavior='terminate',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'wp-curso-python'
                },
                {
                    'Key': 'Ambiente',
                    'Value': 'Desenvolvimento'
                }
            ]
        }
    ]
)
print(resposta_ec2)