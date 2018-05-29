#Import the OpenCV library.
import cv2

#Read a color image
image = cv2.imread('/home/sushantshetty/Documents/test.jpeg',1)
print image

'''The cv2.imread() function is used to read an image. 
The first parameter points to the image. The image should be in 
	the working directory or a full path of image should be given.
	If the image is in the same directory just specify the name of the image.
The second argument is a flag which specifies the way image should be read.
cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

Note: Instead of these three flags, you can simply pass integers 1(COLOR), 0(GRAYSCALE) or -1(UNCHANGED) respectively.

Warning: Even if the path is wrong, cv2.imread() won't show an error. However, cv2.imshow() will show an error since there is 
	no image stored in the variable to be shown.
	To check if the image is loaded properly uncomment line 6. If it outputs an array the image is loaded and there will be no errors.
	However, if it outputs 'None' check the image path properly for typos in the path/name specified.'''

#Display the frame.
cv2.imshow('Image', image)
'''The first parameter is the user defined name for the window that pops up.
The second parameter is the image (the variable in which the image is stored) to be displayed.
'''
 
cv2.waitKey(0)
'''The waitKey function is a keyboard interrupt.
The function waitKey waits for a key event for 'delay' milliseconds 
	before executing the next line of code.
If 0 is passed the code waits infinitely for a keyboard input. '''


	