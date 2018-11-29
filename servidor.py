import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8088))
serversocket.listen(1)
while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if buf != 'END':
        print buf
    else:
      serversocket.close()
      connection.close()
      break

        