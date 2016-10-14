#!/usr/bin/env python

import socket
import ssl
import shutil

#envia um arquivo
def send_file(socket, filename):
    with open('test.txt','rb') as inp:
        out = socket.makefile('wb')
        shutil.copyfileobj(inp, out)


TCP_IP = '127.0.0.1'
TCP_PORT = 7000
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

#socket para o server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#ligacao com tp e porta
s.bind((TCP_IP, TCP_PORT))
#atende chamadas
s.listen(1)

#recebeu uma chamada
conn, addr = s.accept()
#wrap de ssl
connstream = ssl.wrap_socket(conn,
                                 server_side=True,
                                 certfile="selfsigned.cert",
                                 keyfile="selfsigned.key")
print 'Connection address:', addr

#recebe dados do cliente
data = connstream.recv(BUFFER_SIZE)

if data == 'download':
    print "Sending file..."
    data = 'ok'
    #confirma a requisicao do cliente
    connstream.send(data)
    send_file(connstream, "test.txt")

connstream.close()
