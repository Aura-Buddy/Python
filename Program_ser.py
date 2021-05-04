import socket
import time

def main():
	message = ""
	port = 8888

	#establish socket object
	s = socket.socket()

	#connect to anything that is talking on this network on port 8888
	s.bind(('0.0.0.0',port))

	print("waiting for incoming connection\n")	

	#wait for one connection to this socket to proceed
	s.listen(1)
 
	#accepting connection from whomever is attached
	clientsocket,address = s.accept()

	print("connected from {}, port {}\n".format(address,port))

	#informing client how to terminate connection
	clientsocket.send("Welcome to the server!\n Send 'close' to terminate connection".encode('utf-8'))

	while message != "close":
		#Receiving message
		received_message = clientsocket.recv(1024)
		#Decoding message
		decoded_message = received_message.decode('utf-8')
		print("received: {}\n".format(decoded_message))
		#Converting message to uppercase
		modified_message = decoded_message.upper()
		#sending uppercase message to client
		print("sent to client: {}\n".format(modified_message))
		clientsocket.send(modified_message.encode('utf-8'))
		#setting up condition for while loop
		message = decoded_message
	
	s.close()
	print("Connection terminated")
	
main()	
