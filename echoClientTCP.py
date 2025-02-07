import socket
import time

#HOST = '127.0.0.1'
HOST = '192.168.137.141'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	counter = 0
	while True:
		strToSend = "Hello, world-"+str(counter)
		s.sendall(bytes(strToSend,"utf-8"))
		data = s.recv(1024)
		print('Received echo: ', repr(data))
		time.sleep(1)
		counter = counter+1
		
print("finished")