#coding: utf-8

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

'''We construct a NumPy array using the np.zeros() method with 480 rows and 640 columns, 
	yielding a 640 × 480 pixel image. We also allocate space for 3 channels – one for Red, Green, and Blue,
	respectively.
As the name suggests, the zeros method fills every element in the array with an initial value of zero.
Since we are representing our image as an RGB image with pixels in the range [0, 255] , 
	it’s important that we use an 8-bit unsigned integer, or uint8.
''' 
image = np.zeros((480, 640, 3), dtype = "uint8")

#Initialize a colour with the tupple values
white = (255,255,255)
'''This is done to avoid writing the colour parameter values for every drawing operation.
You can use the variable 'white' instead.
'''

#Draw lines using cv2.line() method
cv2.line(image, (0, 0), (640, 480), white, 1)
cv2.line(image, (640, 0), (0, 480), white, 1)
'''The first argument to this method is the image we are going to draw on. In this case, it’s image.
The second argument is the starting point of the line. We choose to start our line from the top-left 
	corner of the image, at point (0, 0) . We also need to supply an ending point for the
	line (the third argument). We define our ending point to be (640, 480) , the bottom-right corner of the image.
The fourth argument is the color of our line, which, in this case, is white.
The final argument is the thickness of the line.
'''

'''Calculates two variables: X and Y.
These two variables represent the ( x, y ) coordinates of the center of the image.
We calculate the center by examining the shape of our NumPy array, and then dividing by two.
The height of the image can be found in image.shape[0] and the width in image.shape[1].
'''
(X, Y)= (image.shape[1] // 2, image.shape[0] // 2)


'''We loop over a number of radius values, starting from 0 and ending at 216(since the range function is
exclusive), incrementing by 24 at each step.'''
for r in range(0, 240, 24):

	#Draw circles using  the cv2.circle() method.
	cv2.circle(image, (X, Y), r, white)
	'''The first parameter is the image on which we want to draw the circle on. 
	We then need to supply the point in which our circle will be drawn around. We pass in a tuple of (X, Y) 
		so that our circles will be centered at the middle of the image. 
	The third argument is the radius of the circle we wish to draw. Finally, we pass in the color of our circle,
		in this case, white.
	'''

#Draw a rectangle using cv2.rectangle() method
cv2.rectangle(image, (104,24),(536,456), white, 1)
'''The first argument is the image we want to draw our rectangle on.
The second argument is the starting ( x, y ) position of our rectangle – here, we are starting our rectangle
at point (104, 24) .
Then, we must provide an ending (x, y) point for the rectangle. We decide to end our rectangle at
(536, 456).
The fourth argument is the color of the rectangle we want to draw.
And the final argument is the thickness of the rectangle.
'''

#Display the frame.
cv2.imshow('Drawing', image)
'''The first parameter is the user defined name for the window that pops up.
The second parameter is the frame (the variable in which the image is stored) to be displayed.
'''

cv2.waitKey(0)
'''The waitKey function is a keyboard interrupt.
The function waitKey waits for a key event for 'delay' milliseconds 
	before executing the next line of code.
If 0 is passed the code waits infinitely for a keyboard input.
'''