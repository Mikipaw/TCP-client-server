# -*- coding: utf-8 -*-
from socket import *
import sys

#serverName = 'hostname'
#serverPort = 12000

BUFFER_SIZE      = 1024
PORT_LOWER_BOUND = 1024
PORT_UPPER_BOUND = 5000

def TCPClient(serverName, serverPort):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    
    sentence = input('Input lowercase sentence:')
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(BUFFER_SIZE)
    
    print("From Server:", modifiedSentence)
    clientSocket.close()
    
    
    # The function checks user-entered parameters for client work
def check_client_params(serverName, portNumber):
    if int(portNumber) > PORT_UPPER_BOUND or int (portNumber) < PORT_LOWER_BOUND:
        print("Port number invalid. Port number should be in range (1024, 5000).")
        return False
    try:
        gethostbyname(serverName)
    except socket.error:
        print("Invalid host name. Exiting.")
        return False
    return True
    

def TCPServer(serverPort):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    
    serverSocket.listen(1)
    print('The server is ready to receive')
    
    while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(BUFFER_SIZE)
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence)
        connectionSocket.close()
    
    
# The function checks user-entered parameters for server work
def check_server_params(serverPort):
    if int(serverPort) > PORT_UPPER_BOUND or int (serverPort) < PORT_LOWER_BOUND:
        print("Port number invalid. Port number should be in range (1024, 5000).")
        return False
    return True        


def PrintInformation():
    print("This program maintains working like a server with TCP socket and like a client.")
    print("If you want to use the program like a server, just enter the server port when you run a program. For example, \"python \"TCP client-server.py\" 2048\"")
    print("If you want to use the program like a client, just enter the server name and port number when you run a program. For example, \"python \"TCP client-server.py\" hostname 2048\"")
    print("Port number must be in range (1024, 5000) to correct execution")
    return
        

if __name__ == '__main__':
    if len (sys.argv) == 3:
        type = check_client_params(sys.argv[1], sys.argv[2]) #checks server name and port number
        if type:
            TCPClient(sys.argv[1], int(sys.argv[2]))
        else:
            print("Invalid input")
            print("Please, enter \"python \"TCP client-server.py\" -help\" to get instructions")

    elif len (sys.argv) == 2: #checks port number
        type = check_server_params(sys.argv[1])
        if type:
            TCPServer(int(sys.argv[1]))
        elif sys.argv[1] == "-help":
            PrintInformation()
        else:
            print("Invalid input")
            print("Please, enter \"python \"TCP client-server.py\" -help\" to get instructions")

    else:
        print("Invalid input! The programm expects 1 or 2 params, but {} were given".format(len(sys.argv) - 1))
        print("Please, enter \"python \"TCP client-server.py\" -help\" to get instructions")
