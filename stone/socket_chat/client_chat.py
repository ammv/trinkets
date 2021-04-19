import socket
import threading


'''SERVER'''
class ChatClient:

    def __init__(self, ip, port):
        self.ip = ip
        print('IP: ', self.ip)

        self.nickname = False
        
        self.port = port
        print('PORT: ', self.port)

        self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        print('socket: ', self.socket)

        self.socket.bind(('', 0))
        

    def read_socket(self):
        while True:
            data = self.socket.recv(1024)
            if '/*useradded' in data.decode('utf-8'):
                self.nickname = data.split()[1]
            print(data.decode('utf-8'))

    def server_send(self):
        data = ('\n' + self.nickname + ' connect to server').encode('utf-8')
        self.socket.sendto(data, (self.ip, self.port))

    def register(self):
        data = 'Неизвестный пользователь подключен к серверу'.encode('utf-8')
        self.socket.sendto(data, (self.ip, self.port))

    def client_send(self, message):
        data = message.encode('utf-8')
        self.socket.sendto(data, (self.ip, self.port))

    def user_send(self, message):
        data = ('\n[{}] {}'.format(self.nickname, message)).encode('utf-8')
        self.socket.sendto(data, (self.ip, self.port))

    def thread(self):
        thr = threading.Thread(target=self.read_socket)
        thr.start()

        

chat = ChatClient('localhost', 8888)
chat.register()
chat.thread()
print('Client connect to server')
while chat.nickname == False:
    message = input()
    chat.client_send(message)

print('nickname :' + chat.nickname)
    
chat.server_send()
while True:
    message = input()
    chat.user_send(message)
        
        
