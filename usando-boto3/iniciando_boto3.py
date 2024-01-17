import boto3

sessao = boto3.Session(profile_name="python-lambda-ricardo")  # cria uma sessão com as credenciais do AWS CLI

cliente_s3 = sessao.client('s3')  # instancia o objeto em uma variavel, tipo como fazíamos com ML
lista = cliente_s3.list_buckets()  # agora a variavel possui os métodos do objeto que foi instanciado nela mesma, neste exemplo, o list buckets


print(lista)

