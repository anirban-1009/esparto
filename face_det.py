import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while 1 :
	ret, img = cap.read()#getting the frame data
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#turning image into a grayscale image
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	#getting the co-ordinates of detected face with the height and width
	#ScaleFactor determines the factor of increase in window size
	# Higher the values of the “minNeighbors”, less will be the number of false positives, and less error will be in terms of false detection of faces

	for (x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)
		#drawing a rectangle around the face
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		#region of interest in gray and color


	cv2.imshow('img',img)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break


cap.release()
cv2.destroyWindows()
