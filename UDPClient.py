import socket
from socket import *
print "Enter the server name"
sname = raw_input()
print "Enter the server port"
sport = input()
clientSocket = socket(AF_INET, SOCK_DGRAM)
i = 1
while i <= 5:
    message = raw_input("Input lowercase sentence:")
    clientSocket.sendto(message,(sname, sport))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print modifiedMessage
    i = i+1
clientSocket.close()