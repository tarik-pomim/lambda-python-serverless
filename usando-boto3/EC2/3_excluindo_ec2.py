import boto3

sessao = boto3.Session(profile_name="python-lambda-ricardo")
cliente_ec2 = sessao.client('ec2')

id_instancia = 'i-014d3ce9778a090f5'  # listado na aula 2_parando_iniciando_ec2.py

# excluindo instancia INCLUINDO EBS CUIDADO:
cliente_ec2.terminate_instances(
    InstanceIds=[id_instancia]
)