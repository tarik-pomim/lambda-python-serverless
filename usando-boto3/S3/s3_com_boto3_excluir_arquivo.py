import boto3

sessao = boto3.Session(profile_name="python-lambda-ricardo")

nome_bucket = 'lambda-tarik'

# client
cliente_s3 = sessao.client('s3')

# resource
resource_s3 = sessao.resource('s3')
bucket = resource_s3.Bucket(nome_bucket)

# usando o delete_objects
# resposta_delete = bucket.delete_objects(
#     Delete={
#         'Objects': [
#             {
#             'Key': 'planilha.xls'
#             },
#             {
#             'Key': 'anotacoes.txt'
#             }
#         ]
#     }
# )
# print(resposta_delete)

# listando e deletando todos os objetos **PERIGO** tanto pra custo devido a requisiçoes quanto a exclusao permanente
# objetos = bucket.objects.all()
# # for obj in objetos:
# #     print(obj)
# resultado = objetos.delete()  # **PERIGO**
# print(resultado)

# utilizando delete_object - cuidado ao usar pois apaga sem confirmação alguma
# resposta = cliente_s3.delete_object(
#     Bucket=nome_bucket,
#     Key='logs/logs_intro_python.txt'
# )
# print(resposta)
