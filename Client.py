# -*- coding: utf-8 -*-
"""


@author: sewar khalifeh
Socket programming with UDP for Client Server instant communication
Transfering through UDP Model is unreliable but fast"""

import socket #include Python’s socket library
serverPort = 19999
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
message = input(str('Input lowercase sentence:')) #get user input 
clientSocket.sendto(message,serverPort) #Attach server port to message; send to server socket
newMessage, serverAddress = clientSocket.recvfrom(2048) 
print (newMessage) 
clientSocket.close() 
