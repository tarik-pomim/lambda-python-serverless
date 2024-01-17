import boto3

sessao = boto3.Session(profile_name="python-lambda-ricardo")

nome_bucket = 'lambda-tarik'

# client
cliente_s3 = sessao.client('s3')

# resource
resource_s3 = sessao.resource('s3')
bucket = resource_s3.Bucket(nome_bucket)

#cliente_s3.delete_bucket(Bucket=nome_bucket)  # usando client
bucket.delete()  # usando resource

