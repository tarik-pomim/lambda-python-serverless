import boto3

sessao = boto3.Session(profile_name="python-lambda-ricardo")
cliente_ec2 = sessao.client('ec2')

# listando instancias que estão rodando no momento:
resposta_instancias = cliente_ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
                'stopped'
            ]
        }
    ]
)
# print(resposta_instancias)
# este caminho ele usou o debug pra pescar, para info vá ao curso sessão 5 video 55:
id_instancias = resposta_instancias['Reservations'][0]['Instances'][0]['InstanceId']

print(id_instancias)

# parando instances:
# cliente_ec2.stop_instances(InstanceIds=[id_instancias])

# ligando instances:
cliente_ec2.start_instances(InstanceIds=[id_instancias])