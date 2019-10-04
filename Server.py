# -*- coding: utf-8 -*-
"""


@author: Sewar khalifeh
Socket programming with UDP for Client Server instant communication
Transfering through UDP Model is unreliable but fast
"""

import socket
serverPort = 19999
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP socket 
serverSocket.bind(('', serverPort)) #bind socket to local port 19999 
print ("server ready")
while True:
 message, clientAddress = serverSocket.recvfrom(2048) 
 newMessage = message.upper() #converts to uppercase
 serverSocket.sendto(newMessage, clientAddress) #send upper case  back to client 