import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 50015))


while True:
    msg = str(input('Was moechten Sie dem Server sagen? '))
    msg = msg.encode()
    s.send(msg)

    msg = s.recv(1024)
    msg = msg.decode()
    print('Serverantwort: '+msg)


s.close()