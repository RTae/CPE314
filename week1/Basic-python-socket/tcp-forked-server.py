from socket import * 
import sys
import os

SERV_PORT = 50000

addr = ('127.0.0.1', SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)
s.bind(addr)
s.listen(1)
print ('TCP forked server started ...')

while True:
  sckt, addr = s.accept()
  ip, port = str(addr[0]), str(addr[1])
  print ('New client connected from ..' + ip + ':' + port)
 
  if os.fork() == 0: 
     while True:
       txtin = sckt.recv(1024)
       print ('Client> %s' %(txtin).decode('utf-8')) 
       if txtin == b'quit':
         print('Client disconnected ...')
         break
       else:
         txtout = txtin.upper()    
         sckt.send(txtout)
     sckt.close()
  else:
     sckt.close()
  
s.close()
