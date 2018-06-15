#Import the OpenCV library
import cv2

#Import the NumPy library 
import numpy as np
'''NumPy is a library for the Python programming language
	that (among other things) provides support for large, multidimensional arrays.
Representing images as NumPy arrays is not only computationally and resource efficient, 
	many other image processing and machine learning libraries use NumPy array 
	representations as well.
Furthermore, by using NumPy's built-in high-level mathematical functions, we can quickly
and easily perform numerical analysis on an image.
'''

'''We construct a NumPy array using the np.zeros method with 480 rows and 640 columns, 
	yielding a 640 × 480 pixel image. We also allocate space for 3 channels – one for Red, Green, and Blue,
	respectively. As the name suggests, the zeros method fills every element in the array 
	with an initial value of zero.
Since we are representing our image as an RGB image with pixels in the range [ 0, 255 ] , 
	it’s important that we use an 8-bit unsigned integer, or uint8.
''' 
image = (np.zeros((480,640,3), np.uint8))
#cv2.imshow('black_image', image)

#Use NumPy array slicing to assign different colours to different slices of the image.
'''Note: OpenCV stores RGB channels in reverse order. While we normally think in terms
	of Red, Green, and Blue, OpenCV actually stores them in the order of Blue, Green, and Red.
	Keep this in mind while assigning values or changing colours. 
''' 
image[:,0:92] = [200,200,200]
image[:,92:184] = [0,255,255]
image[:,184:276] = [255,255,0]
image[:,276:368] = [0,255,0]
image[:,368:460] = [255,0,255]
image[:,460:552] = [0,0,255]
image[:,552:640] = [200,0,75]
'''Since we are recreating a Television Colour Bar we have divided the image into seven sections and 
	assigned colours accordingly.
'''

#Display the frame.
cv2.imshow('Television Colour Bar', image)
'''The first parameter is the user defined name for the window that pops up.
The second parameter is the frame (the variable in which the image is stored) to be displayed.
'''

cv2.waitKey(0)
'''The waitKey function is a keyboard interrupt.
The function waitKey waits for a key event for 'delay' milliseconds 
	before executing the next line of code.
If 0 is passed the code waits infinitely for a keyboard input.
'''

'''For your reference, here are some common colors represented as RGB tuples:
Note: OpenCV stores RGB channels in reverse order. While we normally think in terms
	of Red, Green, and Blue, OpenCV actually stores them in the order of Blue, Green, and Red.
	Keep in mind this thing while assigning values or changing colours. 
Black: (0,0,0)
White: (255,255,255)
Red: (255,0,0)
Green: (0,255,0)
Blue: (0,0,255)
Aqua: (0,255,255)
Fuchsia: (255,0,255)
Maroon: (128,0,0)
Navy: (0,0,128)
Olive: (128,128,0)
Purple: (128,0,128)
Teal: (0,128,128)
Yellow: (255,255,0)'''