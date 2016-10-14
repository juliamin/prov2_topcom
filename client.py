#!/usr/bin/env python

import socket
import ssl
import shutil


def recv_file(socket, filename):
    with open('download.txt','wb') as out:
        inp = socket.makefile('rb')
        shutil.copyfileobj(inp, out)
        out.close()

TCP_IP = '127.0.0.1'
TCP_PORT = 7000
BUFFER_SIZE = 1024

#socket para o cliente
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#wrap do socket
ssl_sock = ssl.wrap_socket(s,
                           ca_certs="selfsigned.cert",
                           cert_reqs=ssl.CERT_REQUIRED)

ssl_sock.connect((TCP_IP, TCP_PORT))

#pede pelo download do arquivo
ssl_sock.send("download")

#recebe a resposta do servidor
data = ssl_sock.recv(BUFFER_SIZE)

if data == "ok":
	print "Downloading..."
	#recebe o arquivo
	recv_file(ssl_sock, "download.txt")

ssl_sock.close()