from cv2 import cv
import cv2
import numpy as np
from time import sleep

def anaglyph(first, second):

	a, b, c = cv2.split(first)
	d, e, f = cv2.split(second)

	return cv2.merge((a, f, e))

def main():

	cam2 = cv2.VideoCapture(0)
	cam1 = cv2.VideoCapture(1)
	# Two cameras connected

	cv2.namedWindow("win")
	ret, first = cam1.read()
	ret, second = cam2.read()
	merge = anaglyph(first, second)
	cv2.imshow("win", merge)
	cv2.waitKey(20)

	while True :
		ret, first = cam1.read()
		ret, second = cam2.read()
		merge = anaglyph(first, second)
		cv2.imshow("win", merge)

		if cv2.waitKey(20) == 27:
			break

	cv2.destroyAllWindows()

if __name__=="__main__":
	main()