import socket

HOST = '127.0.0.1' 
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	print("Lstening on ", HOST, PORT)
	s.listen()
	while True:
		(conn, addr) = s.accept()
		print("Connection accepted from:", addr)
		with conn:
			while True:
				try:
					data = conn.recv(1024)
					decoded = data.decode()
					print("Received ", decoded)
					conn.sendall(data)
				except:
					print("Connection error, continue listening..")
					break			