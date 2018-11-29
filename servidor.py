import socket

from Central import Central
# from Cpu import Cpu
# from Impresora import Impresora
from Memoria import Memoria
from MemoriaAlloc import MemoriaAlloc
from Proceso import Proceso


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8088))
serversocket.listen(1)
while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if buf != 'END':
        handleMessage(buf)
    else:
      serversocket.close()
      connection.close()
      break

def handleMessage(buf):


        