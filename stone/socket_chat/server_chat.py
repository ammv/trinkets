import socket


'''SERVER'''
class ChatServer:

    def __init__(self, ip, port):
        self.ip = ip
        print('IP: ', self.ip)
        
        self.port = port
        print('PORT: ', self.port)
        
        self.socket = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
        print('socket: ', self.socket)
        
        self.socket.bind((self.ip, self.port))
        print('binded...')
        
        self.clients = {}
        self.users = []

    def start(self):
        print('server started')
        while True:
            
            data , addres = self.socket.recvfrom(1024)
            print ('connect: ', addres[0], addres[1])
            if addres[0] not in self.clients: 
                self.clients[addres[0]] = 0
                
            if self.clients[addres[0]] == 0:
                message = 'Придумайте себе никнейм'.encode('utf-8')
                self.socket.sendto(message, addres)
                
                if data.decode('utf-8') in self.users:
                    error = 'Данный никнейм уже занят'.encode('utf-8')
                    self.socket.sendto(error, addres)
                    
                else:
                    self.clients[addres[0]] == 1
                    self.users.append((data.decode('utf-8'), addres))
                    
                    answer = 'Вы зарегистрированы, добро пожаловать!'.encode('utf-8')
                    self.socket.sendto(answer, addres)
                    
                    data2 = data.decode('utf-8')
                    accept = ('/*useradded ' + data2).encode('utf-8')
                    self.socket.sendto(accept, addres)

            print('клиенты: ', self.clients)
            print('длина: ', len(self.users),'\nхуюзеры: ',self.users)
            for user in self.users:
                if user == user[1]:
                    continue
                self.socket.sendto(data, user)

chat = ChatServer('localhost', 8888)
chat.start()        
        
