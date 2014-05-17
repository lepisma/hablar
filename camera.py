"""
Camera handling
"""

import cv2

def make_anaglyph(first, second):
	"""
	Merge two images to create anaglyph image
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