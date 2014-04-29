# Connections handling

import socket
import threading

#---------------------------------
# Defines a network thread
class network_thread(threading.Thread):
	def __init__(self, target, *args):
		self._target = target
		self._args = args
		threading.Thread.__init__(self)

	def run(self):
		self._target(*self.args)

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