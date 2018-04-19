import socket
from socket import *

seport = input("please enter serverPort number: ")
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', seport))
print "The server is ready to receive"
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.upper()
    modifiedMessage = "FROM SERVER SIDE: " + modifiedMessage
    serverSocket.sendto(modifiedMessage, clientAddress)