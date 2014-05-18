#!/usr/bin/python

"""
hablar 3D chat main file
"""

import socket
import argparse
from connections import MasterThread, ClientThread

CONNECTION_PORT = 1111

def hablar_master(port):
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
	
	MasterThread(conn, 'receive').start()
	
	# Start a send stream thread
	conn, details = server.accept()
	
	print "+++ Starting send thread. . ."
	
	MasterThread(conn, 'send').start()
	
	
def hablar_client(host, port):
	"""
	I am joining a chat session
	"""
	
	print "+++ Starting send thread. . ."
	
	# Start a send stream thread
	ClientThread(host, port, 'send').start()
	
	print "+++ Starting receive thread. . ."
	
	# Start a receive stream thread
	ClientThread(host, port, 'receive').start()


# ------------------------------------------------------------------------------------
# Command line arguments

parser = argparse.ArgumentParser(description = 'Hablar is a 3D video chat application.')
parser.add_argument('-m', '--mode',
				help = "Set the mode of hablar: either 'master' (you are setting up the call) or 'client' (you are invited to a call)",
				required = True)
parser.add_argument('-s', '--master',
				help = 'Set the master IP')
args = vars(parser.parse_args())

if args['mode'] == 'master':
	hablar_master(CONNECTION_PORT)

elif args['mode'] == 'client':
	if args['master']:
		hablar_client(str(args['server']), CONNECTION_PORT)
	else:
		hablar_client('localhost', CONNECTION_PORT)