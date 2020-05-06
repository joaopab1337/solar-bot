import requests
import random

from config import TELEGRAM_SEND_MESSAGE_URL

def send_message(chat_id, content):
    url = TELEGRAM_SEND_MESSAGE_URL.format(chat_id, content)
    req = requests.get(url)
    return True if req.status_code == 200 else False

def ednaldo(request):
    message = request['message']
    chat_id = message['chat']['id']
    user = message['from']['first_name']
    
    response_messages = [
        'Este cara não canta porra nenhuma e ele tem que cantar é no inferno.',
        'Um alô para {}'.format(user),
        'É isso aí galera, continuem se inscrevendo no canal de Ednaldo Pereira',
        'Pum pum pum puntsssssssssssss',
        'Punts pum pum'
    ]

    content = random.choices(
        response_messages,
        weights = [1, 2, 2, 4, 4],
        k=1
    )
    

    return send_message(chat_id, content[0])

def invalid_action(request):
    message = request['message']
    chat_id = message['chat']['id']
    user = message['from']['first_name']
    response_messages = [
        'Ô mizera, o que é que tu quer?',
        'Sou burro. Sei o que é isso não.',
        'Querido {}, é pra digitar com os dedos, não é pra dar testada no teclado não.'.format(user),
        'Digita direito carai.',
        'Ação inválida.'
    ]

    content = random.choices(
        response_messages,
        weights = [1, 2, 2, 4, 10],
        k=1
    )
    
    return send_message(chat_id, content[0])



