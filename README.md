# webserver
This is my code for my course at UTSA - Computer Networks - Spring 2024
Below is the description of the assignment

# Develop a Web server in Python
Develop a Web server using TCP socket programming in Python. You will demonstrate how to
create a socket, bind it to a specific address and port, connect to another application, and send
and receive HTTP packets. You will also learn some basics of HTTP header format. Use Python
to develop your program. Do not use any HTTP packages or any online sources for code
development. See [KR] Section 2.7, for example, TCP client and server codes.

# Web Server Specifications
Develop a non-persistent web server that handles one HTTP request at a time. Your web server
should accept and parse the HTTP request, get the requested file from the server’s file system,
create an HTTP response message consisting of the requested file preceded by header lines, and
then send the response directly to the client.
If the requested file is not in the server, the server should send an HTTP “404 Not Found”
message back to the client. Either way, the server should return to the listening mode and repeat
the accept and respond sequence.
The server should terminate if an interrupt signal (^c) is received from the keyboard gracefully.
Also, the server should terminate if the client requests a file named “stop” (without the quotes,
not case-sensitive) with any extension and the file does not exist.
Below, you will find the skeleton code for the Web server. Complete the skeleton code to get a
rudimentary version of the server. The places where you need to fill in the code are marked with
#Fill-in-start and #Fill-in-end. Each place may require one or more lines of code.
However, the skeleton code does not check and catch most errors during execution. Revise the
code to catch possible errors and handle them. Document your code thoroughly so that the logic
is understandable by someone knowledgeable in networks but not an expert in Python or network
application programming. The code should be efficient and eliminate unnecessary duplication of
logic.
The format for running your Web server:
$ python3 Webserver.py serverPort

# Web Client
A functional Web client is provided with some error checking but very little documentation. This
Web client sends an HTTP GET request for a file to the server you developed in part 1, displays
the response from the server, and stops execution. You may use this client to test your Web
server functionality.
The format for running your Web client:
$ python3 Webclient.py serverAddress serverPort filename
Networks Programming Assignment
Instructor: Rajendra V. Boppana 240131 2

# Checking the Server Code
Put an HTML file (e.g., HelloWorld.html) in the same directory that the server is in. Run the
server program that listens and accepts connection requests received at a port, say “serverPort,”
specified through command line arguments. (The 16-bit port numbers are grouped into well-
known, user-defined, and ephemeral ports. Use an appropriate port for your server to listen to
and accept client requests.) Determine the host’s IP address running the server (e.g.,
10.100.240.202 for fox02.cs.utsarr.net).
You can check the working of your server program using a Web browser, the client provided, or
the wget command (on Linux machines. For example, open a browser from another or the same
host and provide the corresponding URL. For example:
http://10.100.240.204:serverPort/HelloWorld.html
‘HelloWorld.html’ is the file you placed in the server directory. Note also the use of the port
number after the colon. This is the port number where the server application listens and accepts
clients’ connection requests. The browser should then display the contents of HelloWorld.html.
Then, try to get a file not present on the server. You should get a “404 Not Found” message.
Try to stop the server by having the client send a request to the server for the URL:
http://10.100.240.204:serverPort/stop
Also, stop the server by sending a keyboard interrupt (^c) to the server process.
