from socket import * #import socket module
import sys # In order to terminate the program
import errno
import os

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverPort = int(sys.argv[1]) 

#Fill in start
try:
	serverSocket.bind(('', serverPort))
	serverSocket.listen(1)
	print("The web server is up on port:", serverPort)
except Exception as e:
	print("failed to start the server:", e)
	sys.exit(1)
try:
	#Fill in end
	while True:
		#Establish the connection
		print('Ready to serve...')
		connectionSocket, addr = serverSocket.accept()  #Fill in start 	 #Fill in end
		try:
			message = connectionSocket.recv(1024) #Fill in start 	 #Fill in end
			filename = message.split()[1][1:].decode()

			if filename.lower() == "stop" or filename.lower() == "/stop":
				print("Server stopped by client request.")
				connectionSocket.send("\nHTTP/1.1 200 OK\n\n".encode())
				connectionSocket.close()
				serverSocket.close()
				break

			if os.path.exists(filename):
				with open(filename, 'rb') as f:
					outputdata = f.read() #Fill in start #Fill in end
					#print(outputdata)
					#Send one HTTP header line into socket
					#Fill in start
					connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
					#Fill in end
					#Send the content of the requested file to the client
					for i in range(0, len(outputdata)):
						connectionSocket.send(outputdata[i:i+1])
					connectionSocket.send("\r\n".encode())

			else:
				raise IOError("file not found")
			connectionSocket.close()

		except IOError:
			#Send response message for file not found
			#Fill in start
			response = "HTTP/1.1 404 Not Found\r\n\r\n <html><head><title>404 Not Found</title></head><body><h1>404 Not Found</h1></body></html>"
			connectionSocket.send(response.encode())
			#Fill in end
			#Close client socket
			#Fill in start
			connectionSocket.close()
		except Exception as e:
			print(f"Error: {e}")
			connectionSocket.close()
			#Fill in end
except KeyboardInterrupt:
	print("\nServer stopped by Keyboard Interrupt\n\nGraceful shutdown..\n")
serverSocket.close()
sys.exit()
