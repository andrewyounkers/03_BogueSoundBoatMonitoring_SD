#!/usr/bin/env python3
import socket

s = socket.socket()
#host = socket.gethostname()
host = '192.168.24.152'
print (host)
port = 12345
file = open("test.txt", "w")

s.connect((host, port))
data = s.recv(409600)
print (data)
file.write(str(data))
s.close
file.close()