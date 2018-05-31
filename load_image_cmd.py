#Import the OpenCV library
import cv2

#Import the argparse module
import argparse
'''The "argparse" is a command-line parsing module in the Python Standard Library.
The argparse module makes it easy to write user-friendly command-line interfaces.
The program defines what arguments it requires, and argparse will figure out how
	to parse those out of sys.argv. 
The argparse module also automatically generates help and usage messages and
	issues errors when users give the program invalid arguments.
'''

#Create an object 'parser' of class ArgumentParser()
parser = argparse.ArgumentParser(description = 'Load image using the command prompt')
'''This constructor takes several arguments to set up the description used in the 
	help text for the program and other global behaviors or settings.
Type "python load_image_cmd.py -h" in the command prompt to see this message along 
	with other available arguments.
'''

#Defining Arguments
parser.add_argument("-i","--image",required = True, 
	help = "Path to the image or name of the image if it is in the same directory")
'''In this command you can specify which arguments are needed from the command line.
'''

#
args = vars(parser.parse_args())
'''The parse_args() function will take the arguments you provide on the command line 
	when you run your program and interpret them according to the arguments you have 
	added to your ArgumentParser object.
The return value from parse_args() is a Namespace containing the arguments to the command.
The vars() function returns a dictionary that represents a symbol table: its keys are variable
	names, and each key's corresponding value is its bound value.
The output of print statements on line 36 and 38 will explain the above command more clearly.
'''
print parser.parse_args()

print args

#Read the color image
image = cv2.imread(args["image"],1)
'''The path specified in the imread() function is stored as the value of key "image" in the 
	dictionary "args".
You can change the second parameter '1' to '0' for a grayscale image. 
'''

#Display the image
cv2.imshow("Original", image)

cv2.waitKey(0)
'''The waitKey function is a keyboard interrupt.
The function waitKey waits for a key event for 'delay' milliseconds 
	before executing the next line of code.
If 0 is passed the code waits infinitely for a keyboard input. '''


'''
Usage Example:

python load_image_cmd.py -h (See the description and the available arguments)
python load_image_cmd.py -i "Path to the image/Name of the image if it is in the same directory"
python load_image_cmd.py --image "Path to the image/Name of the image if it is in the same directory"

'''