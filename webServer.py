from socket import * #import socket module
import sys # In order to terminate the program
import errno
import os

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverPort = 6789

#Fill in start
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The web server is up on port:", serverPort)
#Fill in end
while True:
	#Establish the connection
	print('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()  #Fill in start 	 #Fill in end
	try:
		message = connectionSocket.recv(1024) #Fill in start 	 #Fill in end
		filename = message.split()[1][1:]
		
		if filename.lower() == "stop":
			print("Server stopped by client request.")
			connectionSocket.send("\nHTTP/1.1 200 OK\n\n".encode())
			connectionSocket.close()
			serverSocket.close()
			break

		f = open(filename[1:])
		outputdata = f.read() #Fill in start #Fill in end
		print(outputdata)
		#Send one HTTP header line into socket
		#Fill in start
		connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
		#Fill in end
		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode())
		connectionSocket.close()

	except IOError:
		#Send response message for file not found
		#Fill in start
		connectionSocket.send("\nHTTP/1.1 404 Not Found\n\n".encode())
		#Fill in end
		#Close client socket
		#Fill in start
		connectionSocket.close()
	except Exception as e:
		print(f"Error: {e}")
		connectionSocket.close()
		#Fill in end
serverSocket.close()
sys.exit()
