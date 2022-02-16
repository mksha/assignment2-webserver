# import socket module
from socket import *
# In order to terminate the program
import sys
from urllib import response


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serverSocket.bind(("", port))
  #Fill in start
  serverSocket.listen(1)
  # print("Server is ready to listen the requests")
  #Fill in end

  while True:
    #Establish the connection
    # print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:

      try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        
        #Send one HTTP header line into socket.
        #Fill in start
        response_headers = {
          'Content-Type': 'text/html; charset=UTF-8',
          'Content-Length': len(outputdata)
        }
        response_headers_raw = ''.join(f"{k}: {v}\n" for k, v in response_headers.items())


        server_http_version = 'HTTP/1.1'
        status_code = '200'
        status_phrase = 'OK'
        http_status_line = f"{server_http_version} {status_code} {status_phrase}\n"
        connectionSocket.send(http_status_line.encode())
        connectionSocket.send(response_headers_raw.encode())
        connectionSocket.send('\n'.encode())

        #Fill in end

        #Send the content of the requested file to the client
        # print(outputdata.encode())
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        # Send response message for file not found (404)
        #Fill in start
        server_http_version = 'HTTP/1.1'
        status_code = '404'
        status_phrase = 'Not Found'
        http_status_line = f"{server_http_version} {status_code} {status_phrase}\n"
        connectionSocket.send(http_status_line.encode())
        connectionSocket.send("\r\n".encode())
        #Fill in end


        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
