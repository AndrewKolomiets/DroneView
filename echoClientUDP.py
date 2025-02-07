import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address = '127.0.0.1'
server_address = '192.168.137.141'
server_port = 31337
client_socket.connect((server_address, server_port))

message = 'Hello World'
while True:
	client_socket.send(message.encode())
	response = client_socket.recv(1024).decode()
	print("Test passed" if message == response else "Test failed")
	time.sleep(1)