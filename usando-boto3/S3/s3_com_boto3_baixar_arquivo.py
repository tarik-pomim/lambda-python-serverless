import boto3

sessao = boto3.Session(profile_name="python-lambda-ricardo")
cliente_s3 = sessao.client('s3')

nome_bucket = 'lambda-tarik'


# # metodo download_file
# cliente_s3.download_file(
#     nome_bucket,
#     'logs/logs_intro_python.txt',
#     'arquivos/log_boto3.txt'
# )

# # metodo download_fileobj
# arquivo = open('arquivos/log_dois.txt', 'wb')  # wb - write binary
# cliente_s3.download_fileobj(
#     nome_bucket,
#     'logs/logs.jpg',
#     arquivo
# )
# arquivo.close()

# metodo get_object
planilha_s3 = cliente_s3.get_object(
    Bucket=nome_bucket,
    Key='planilha.xls'
)
planilha_body = planilha_s3['Body']
planilha = planilha_body.read()
print(type(planilha))
print(planilha)
print(planilha.decode('utf8'))
