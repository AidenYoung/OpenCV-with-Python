#Import the OpenCV library.
import cv2

#Create an object "cam" of class "VideoCapture".
cam = cv2.VideoCapture(0)
'''VideoCapture is a class for video capturing from video files, 
image sequences or cameras.
The parameter passed is the camera index.
If a single camera is connected pass 0.
For systems with multiple cameras change the index values
'''

#cam.open
'''Explained later'''

#The "while" loop captures each frame and displays it continuosly.
while cam.isOpened():
	'''Sometimes declaration of 'cam' may not initialize the video capture.
	The isOpened function checks if it is initialized and returns 
		True if video capture has started.
	If the code shows error on line 17 it means that video capture is not 
		initialized. 
	To make the code work use cam.open on line 12 and 13.
	'''
	

	#Read the frame captured by 'cam' object.
	ret, frame  = cam.read()
	'''frame stores each corresponding frame, while ret returns a boolean 
		value indicating if the frame was captured properly.
	Even if ret is False, the code will run but frame won't store anything and throw an 
		error while displaying the image.
	To avoid this error, use the codes on line 36-38 and comment line 41. 
	'''

	#if ret == True:

		#cv2.imshow('frame', frame)

	#Display the frame.
	cv2.imshow('frame', frame)
	'''The first parameter is the user defined name for the window that pops up.
	The second parameter is the frame (the variable in which the image is stored) to be displayed.
	'''

	if cv2.waitKey(1) == 27:
		'''The waitKey function is a keyboard interrupt.
		The function waitKey waits for a key event for 'delay'(here 1 millisecond) milliseconds 
			before executing the next line of code.'''

		#Close the capturing device.
		cam.release()
		
		#Destroy the window formed.
		cv2.destroyWindow('frame')
		
		break

		'''In the above code if the Escape key is pressed(27 is the code for Escape) the code
		    closes the capturing device, closes all the windows created during the execution of the program 
		    and breaks out of the while loop.
		'''
