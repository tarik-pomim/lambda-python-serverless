import boto3

sessao = boto3.Session(profile_name="python-lambda-ricardo")

# client
cliente_s3 = sessao.client('s3')
cliente_ec2 = sessao.client('ec2')

lista = cliente_s3.list_buckets()
#print(lista)

# resource
recurso_s3 = sessao.resource('s3')
bucket = recurso_s3.Bucket('tarik.pomim')
print(bucket)

### Para diferença entre client e resource ver sessao 5 aula 46
### Basicamente: client acessa a API da aws diretamente, e resource instancia os métodos/objetos para uma programação mais refinada