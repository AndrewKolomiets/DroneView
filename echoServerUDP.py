import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '192.168.168.40'
#server_address = '192.168.137.1'
#server_address = '172.16.87.168'
server_port = 20200

server = (server_address, server_port)
sock.bind(server)
print("Listening on " + server_address + ":" + str(server_port))

while True:
	payload, client_address = sock.recvfrom(4096)
	print("from" + str(client_address) + " received \n" + str(payload) )
	#print("Echoing data back to " + str(client_address))
	#sent = sock.sendto(payload, client_address)
