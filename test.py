import socket
import sctp
import time

PORT = 5432

sk = sctp.sctpsocket_tcp(socket.AF_INET)

sk.bind(('127.0.0.1', PORT))
sk.listen(1)

print('listening on localhost:' + str(PORT))

client_sk, _client = sk.accept()

client_sk.send('conectou!\n'.encode('utf-8'))

ping = None

while ping != 'close':
    ping = client_sk.recv(1024).decode('utf-8')
    pong = '--> ' + ping
    client_sk.send(pong.encode('utf-8'))

client_sk.close()
sk.close()

