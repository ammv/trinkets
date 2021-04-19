import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
from vk_messages import MessagesAPI
from vk_messages.utils import get_random
from time import sleep

server1 = 'https://www.gs4u.net/ru/s/86698.html'
server2 = 'https://www.gs4u.net/en/s/163316.html'
server3 = 'https://www.gs4u.net/ru/s/165951.html'

servers = [server1, server2, server3]

def _online(url):
    ua = UserAgent().random
    sleep(1)
    
    text = requests.get(url, headers = {'User-agent': ua}).text
    soup = bs(text, 'lxml')

    div_info = soup.find('div', class_ = 'inlineblocktop baseinfo')
    div_fluid = div_info.find_all('div', class_='row-fluid')[4]
    _text = div_fluid.find('div', class_='text')
    online = _text.find_all('b')
    return ' - Онлайн :' + online[0].text.strip() + '\\' + online[1].text.strip()  

def _players(url):
    ua = UserAgent().random
    sleep(1)

    text = requests.get(url, headers = {'User-agent': ua}).text
    soup = bs(text, 'lxml')

    div_info = soup.find('div', id = 'tabs-inner-serverplayers')
    table = div_info.find('table', class_='serverplayers tablesorter table table-striped table-hover')
    _text = table.find('tbody').find_all('tr')
    players = ''.join(' - ' + player.find('td').text + '\n' for player in _text)
    print(players)
    return players

def _servers():
    ua = UserAgent().random
    sleep(1)

    url = 'https://vk.com/untmirage'
    text = requests.get(url, headers = {'User-agent': ua}).text
    soup = bs(text, 'html.parser')
    div_0 = soup.find_all('div', class_='module_body clear_fix')
    k = 0
    for i in div_0:
        if 'Classic | kits/tpa | No Mods' in i.text:
            servers_ = i.text.replace('\n', '').split('Mirage')[1:len(div_0)]
            break
        k += 1

    server_info = ''
    k = 1
    online = 0
    for server_ in servers_:
        i = server_.find('Игроки')
        server_info += 'Сервер {}: {}\n'.format(k, server_[i:len(server_)].split(': ')[1])

        online += int(server_[i:len(server_)].split(': ')[1].split(' / ')[0])
        k += 1

    server_info += 'Общий онлайн {}/{}'.format(online, len(servers_)*24)
    return server_info.lstrip().rstrip()


def send(text):
    global messages
    messages.method('messages.send', peer_id='2000000076', message=text,
            random_id=get_random())

login, password = 'login', 'password'                                
messages = MessagesAPI(login=login, password=password,
                                two_factor=False, cookies_save_path='sessions/')

ids = []

while True:
    history = messages.method('messages.getHistory', peer_id='2000000076', count=5)
    _messages = [(i['text'], i['from_id'], i['id']) for i in history['items']]
    for message in _messages:
        if message[2] not in ids:
            try:
                if message[0] == '!servers':
                    ids.append(message[2])
                    send(_servers())
                elif message[0][:7] == '!server':
                    ids.append(message[2])
                    server = int(message[0].split()[1])-1
                    if server < 3:
                        text = 'Сервер:\n - {}\nОнлайн:\n{}\nИгроки:\n'.format(server+1, _online(servers[server]))
                        text += _players(servers[server])
                        send(text)
            except: pass
    sleep(3)
