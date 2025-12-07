import socket
import time

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
port = 9999
# bind to the port
serversocket.bind((host, port))
# queue up to 5 requests
serversocket.listen(5)
# establish a connection
while True:
    clientsocket, addr = serversocket.accept()
    print("Connected with[addr],[port]%s" % str(addr))
    message = "Hello World\r\n"
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()
