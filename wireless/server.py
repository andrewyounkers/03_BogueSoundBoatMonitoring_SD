#!/usr/bin/env python3
import socket
from datetime import date

s = socket.socket()
#host = socket.gethostname()
host = '172.20.10.9'
port = 12345
s.bind((host, port))

today = date.today()
date = today.strftime("%m-%d")
file = "BoatCount_{}.csv" .format(date)

s.settimeout(5)
s.listen(5)
while True:
  c, addr = s.accept()
  print ('Got connection from',addr)
  f = open(file, 'rb')
  l = f.read(409600)
  while True:
    c.send(l)
    break
  c.close()