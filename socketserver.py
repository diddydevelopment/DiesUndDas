import socket


#192.168.0.1
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print('waiting for client')
serversocket.bind( ('127.0.0.1', 50015) )
serversocket.listen(0)

(clientsocket,adress) = serversocket.accept()
print('client connected')


while True:
    msg = clientsocket.recv(1024)
    msg = msg.decode()
    print(msg)

    ans = 'server hat folgende anfrage bekommen: '+msg
    ans = ans.encode()
    clientsocket.send(ans)


clientsocket.close()
serversocket.close()