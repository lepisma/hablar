"""
Camera handling
"""

import cv2
import numpy

def make_anaglyph(first, second):
	"""
	Merges two images to create anaglyph image
	"""
	
	a, b, c = cv2.split(first)
	d, e, f = cv2.split(second)

	return cv2.merge((a, f, e))

def two_cameras():
	"""
	Returns True if two cameras are found
	"""
	
	# Camera streams
	CAPTURE_1 = cv2.VideoCapture(0)
	CAPTURE_2 = cv2.VideoCapture(1)

	capture_1_flag = CAPTURE_1.retrieve()[0]
	capture_2_flag = CAPTURE_2.retrieve()[0]

	if (capture_1_flag == False) or (capture_2_flag == False):
		print "Not enough cameras found"
		if capture_2_flag == False:
			print "- Check if you attached the second camera"
		if capture_1_flag == False:
			print "- Your primary camera isn't working properly"

		CAPTURE_1.release()
		CAPTURE_2.release()

		return False
	else:
		print "Two cameras found"
		CAPTURE_1.release()
		CAPTURE_2.release()
		
		return True
		
def stream_from(conn):
	"""
	Streams video data from a socket and displays it
	"""
	
	stream_data = conn.recv(1024)
	
	image_string = ''
	
	while stream_data:
		
		if stream_data != 'done':
			image_string += stream_data
		else:
			numpy_data = numpy.fromstring(image_string, dtype = 'uint8')
			image_string = ''
			image = cv2.imdecode(numpy_data, 1)
			cv2.imshow('Stream', image)
			if cv2.waitKey(20) == 27:
				conn.close()
				break
		stream_data = conn.recv(1024)
		

def stream_to(conn):
	"""
	Sends video data from host to remote
	"""
	
	if two_cameras() == True:
		CAMERAS = 2
		CAPTURE_1 = cv2.VideoCapture(0)
		CAPTURE_2 = cv2.VideoCapture(1)
		
		ret_1, frame_1 = CAPTURE_1.read()
		ret_2, frame_2 = CAPTURE_2.read()
		
	else:
		CAMERAS = 1
		CAPTURE_1 = cv2.VideoCapture(0)
		
		ret_1, frame_1 = CAPTURE_1.read()
		ret_2 = True
		
	while ret_1 and ret_2:
		if CAMERAS == 2:
			frame = make_anaglyph(frame1, frame2)
		else:
			frame = frame_1
		
		encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
		result, imgencode = cv2.imencode('.jpg', frame, encode_param)
		data = numpy.array(imgencode)
		string_data = data.tostring()
	
		conn.send(string_data)
		conn.send('done')
		
		ret_1, frame_1 = CAPTURE_1.read()
		if CAMERAS == 2:
			ret_2, frame_2 = CAPTURE_2.read()
		else:
			ret_2 = True