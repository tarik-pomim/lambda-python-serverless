import boto3

sessao = boto3.Session(profile_name="python-lambda-ricardo")

cliente_s3 = sessao.client('s3')

nome_bucket = 'lambda-tarik'

try:
    resposta_bucket = cliente_s3.create_bucket(
        Bucket=nome_bucket,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-east-2'
        }
    )
    # print(resposta_bucket)

except Exception as erro:
    print('Este bucket já existe.')
    

# enviando arquivo para o s3:
cliente_s3.upload_file('arquivos/log.txt',
nome_bucket,
'logs/logs_intro_python.txt'
)

# criando um arquivo diretamente no bucket:
planilha = """
    Nome\tNota
    Ana\t8
    Mario\t9
    Maria\t7
    Carlos\t10
"""

cliente_s3.put_object(
    Body=planilha,
    Bucket=nome_bucket,
    Key='planilha.xls'
)

