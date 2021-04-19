import vk
from vk_messages import MessagesAPI
from time import sleep
from pyperclip import copy
from vk_messages.utils import get_random

login, password = 'login', 'password'                                
messages = MessagesAPI(login=login, password=password,
                                two_factor=False, cookies_save_path='sessions/')

session = vk.AuthSession('7811741', 'login', 'password', scope='user')
vk_api = vk.API(session)
##members = messages.method('messages.getConversationMembers', peer_id='2000000076')['items'][1:]
##users_ = []
##for i in members:
##    user = i['member_id']
##    if str(user)[0] != '-':
##        user = vk_api.users.get(user_id=user, fields='screen_name',v='5.144')[0]
##        sleep(0.3)
##        if 'screen_name' in user.keys():
##            users_.append(user['screen_name'])

with open('sueta.txt') as f:
    users_ = f.read().split('\n')
    
lohi = ''.join(user + '\n' for user in users_)
ids = []

def send(text):
    global messages
    messages.method('messages.send', peer_id='2000000076', message=text,
            random_id=get_random())

print('start script')


while True:
    try:
        history = messages.method('messages.getHistory', peer_id='2000000076', count=5, v='5.144')
        _messages = [(i['text'], i['from_id'], i['id']) for i in history['items']]
        for message in _messages:
            if message[2] not in ids:
                if message[0] == '/all':
                    send('Список лохов в пути...')
                    sleep(1)
                    send(lohi)
                    ids.append(message[2])
    except Exception as e:
        try:
            send("Попробуй ещё раз")
        except:
            pass
    sleep(3)
