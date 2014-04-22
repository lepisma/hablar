# Connections handling

import socket

# --------------------------------
# Creates socket server
def create_server_here(host, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		sock.bind((host, port))
	except socket.error, msg:
		print 'Bind Failed. Errr Code : ' + str(msg[0]) + ' Message : ' + str(msg[1])
		sys.exit()
	return sock

# --------------------------------
# Connects to socket server
def connect_to(host, port):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except:
		print 'Failed to create Socket'
		sys.exit()
	sock.connect((host, port))
	return sock