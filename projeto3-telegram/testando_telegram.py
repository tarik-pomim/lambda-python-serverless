import requests

bot_token = '6880814911:AAGrlptcp_hnOwM_cAgy4WhCzAuFZVJbTws'
id_canal = '-1002104324296'  

# 1. Acessa o site: https://api.telegram.org/bot6880814911:AAGrlptcp_hnOwM_cAgy4WhCzAuFZVJbTws/getUpdates
# 2. manda msg no canal criado no telegram
# 3. atualiza o site pra obter a id_canal

api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

def enviar_mensagem_telegram(mensagem):

    resposta = requests.post(
        api_url,
        json={
            "chat_id": id_canal,
            "text": mensagem
        }
    )
