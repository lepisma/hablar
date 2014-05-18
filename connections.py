"""
Connections handling
"""

import socket
import threading
import camera

class MasterThread(threading.Thread):
	"""
	Threads to be spawned on the master end of chat session
	"""
	
	def __init__(self, conn, mode):
		"""
		Takes the connection object and mode of data transfer
		"""
		
		self.conn = conn
		self.mode = mode
		threading.Thread.__init__(self)
		
	def run(self):
		"""
		Receives and display video if the mode is 'receive'
		Sends video stream if mode is 'send'
		"""
		
		if self.mode == 'receive':
			camera.stream_from(self.conn)
		elif self.mode == 'send':
			camera.stream_to(self.conn)
			

class ClientThread(threading.Thread):
	"""
	Threads running on client side
	"""
	
	def __init__(self, host, port, mode):
		"""
		Takes host and port of master and direction of data transfer
		"""
		
		self.host = host
		self.port = port
		self.mode = mode
		threading.Thread.__init__(self)
		
	def run(self):
		"""
		Receives and display video if the mode is 'receive'
		Sends video stream if mode is 'send'
		"""
		
		conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		conn.connect((host, port))
		
		if self.mode == 'send':
			camera.stream_to(conn)
		elif self.mode == 'receive':
			camera.stream_from(conn)