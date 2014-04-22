#!/usr/bin/python

# hablar 3D chat main file

# Client send the video stream to the server
# The server previews the stream

import socket
import numpy
import argparse
import cv2
import camera
import connections

#---------------------------
# Becoming server
def hablar_server():
	host = 'localhost'
	port = 11111

	sock = connections.create_server_here(host, port)
	sock.listen(10)
	conn, adr = sock.accept()
	stream_data = conn.recv(1024)

	image_string = ''
	
	while stream_data:

		if stream_data != 'done':
			image_string += stream_data
		else:
			numpy_data = numpy.fromstring(image_string, dtype='uint8')
			image_string = ''
			image = cv2.imdecode(numpy_data, 1)
			cv2.imshow('Stream', image)
			if cv2.waitKey(20) == 27:
				break
		stream_data = conn.recv(1024)

	cv2.destroyAllWindows()


#---------------------------
# Becoming client
def hablar_client(host):
	host = host
	port = 11111

	sock = connections.connect_to(host, port)

	if camera.two_cameras() == True:
		print "Hablar running in 3D mode . . ."

		ret_1, frame_1 = camera.CAPTURE_1.read()
		ret_2, frame_2 = camera.CAPTURE_2.read()

		while ret_1 and ret_2:
			frame = camera.make_anaglyph(frame1, frame2)

			encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
			result, imgencode = cv2.imencode('.jpg', frame, encode_param)
			data = numpy.array(imgencode)
			string_data = data.tostring()

			sock.send(string_data)
			sock.send('done')

			ret_1, frame_1 = camera.CAPTURE_1.read()
			ret_2, frame_2 = camera.CAPTURE_2.read()
	else:
		print "Hablar running in 2D mode"

		ret, frame = camera.CAPTURE_1.read()
		while ret:
			encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
			result, imgencode = cv2.imencode('.jpg', frame, encode_param)
			data = numpy.array(imgencode)
			string_data = data.tostring()

			sock.send(string_data)
			sock.send('done')

			ret, frame = camera.CAPTURE_1.read()

#----------------------------