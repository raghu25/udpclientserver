import socket 
import time
from sys import argv
from socket import *
clientSocket = socket(AF_INET, SOCK_DGRAM)
i=1
minrtt=100000
maxrtt=0
sum = 0
count = 0
total = 0
script, message, gaddress, port = argv
while i<=50:
    try:
        print "sequence number%r:" %i
        itime=time.clock()
        clientSocket.sendto(message,(gaddress, int(port)))
        message, serverAddress = clientSocket.recvfrom(1024) 
        clientSocket.settimeout(1)
    except timeout:
        print "Unsuccessful Ping"
        count = count +1
        i=i+1
        continue
    ftime=time.clock()
    RTT = int((ftime-itime)*1000000)
    print message, serverAddress
    print 'Successfully received message %r from %r with RTT: %r microseconds' %(message, serverAddress, RTT)
    total = total +1
    if maxrtt<RTT:
        maxrtt = RTT
    if minrtt>RTT:
        minrtt=RTT
    sum = sum + RTT
    i=i+1

print '\n sum of all the Rtt: %r ' %sum
print "\n average RTT is %r microseconds" %(sum/total)
print "\n total unsuccessful pings %r" %count
print "\n total number of successful pings %r" %total
success_rate = (i-1-count)*100/(i-1)
loss_rate = 100-success_rate
print '\n success_rate is %r percentage ' %success_rate
print '\n loss_rate is %r percentage' %loss_rate
print '\n minrtt is %r microseconds' %minrtt
print '\n maxrtt is %r microseconds' %maxrtt
clientSocket.close()