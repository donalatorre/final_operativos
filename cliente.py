import socket

def sendMessage(msg):
  clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  clientsocket.connect(('localhost', 8088))
  clientsocket.send(msg)

for i in range(1000):
  sendMessage("aaaa")
sendMessage("END")



