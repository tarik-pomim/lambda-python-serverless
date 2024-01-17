import json

log = '-- Log do Sistema --\n'
log += 'Lendo Arquivo\n'

arquivo = open('dados_lendo_arquivos.json', 'r')  # r = read
info = arquivo.read()
#print(info)

dados = json.loads(info)

log += 'Alterando "casado" para false\n'
dados['casado'] = False

log += 'Gravar novo arquivo\n'
novo_arquivo = open('dados_novo.json', 'w')  # w = write
novos_dados = json.dumps(dados)
novo_arquivo.write(novos_dados)
novo_arquivo.close()

novo_arquivo = open('dados_novo.json', 'a')  # a = append
novo_arquivo.write(', {"teste": "ok}')
novo_arquivo.close()

log += "Adicionando ao novo arquivo.\n"
arquivo_log = open('intro_python/arquivos/log.txt', 'w')  # w = write
arquivo_log.write(log)
arquivo_log.close()

#  vai dar alguns erros pois troquei os arquivos de pasta