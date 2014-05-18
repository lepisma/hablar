#!/usr/bin/python

"""
hablar 3D chat main file
"""

import socket
from connections import MasterThread, ClientThread

def hablar_master(port, qt_label):
	"""
	I am starting session
	"""
	
	print "+++ Firing sockets. . ."
	
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(('localhost', port))
	server.listen(2)
	
	print "+++ Started server. . . Listening"
	
	# Start a receive stream thread
	conn, details = server.accept()
	
	print "+++ Starting receive thread. . ."
	
	MasterThread(conn, 'receive', qt_label).start()
	
	# Start a send stream thread
	conn, details = server.accept()
	
	print "+++ Starting send thread. . ."
	
	MasterThread(conn, 'send', qt_label).start()
	
	
def hablar_client(host, port, qt_label):
	"""
	I am joining a chat session
	"""
	
	print "+++ Starting send thread. . ."
	
	# Start a send stream thread
	ClientThread(host, port, 'send', qt_label).start()
	
	print "+++ Starting receive thread. . ."
	
	# Start a receive stream thread
	ClientThread(host, port, 'receive', qt_label).start()