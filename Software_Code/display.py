#-------------------------------------------------------------
#			FUNCTION TO DISPLAY NUMBERS
#			---------------------------
#
# This function displays a two-digit number on the LED matrix
# without scrolling the display. The number to be displayed and
# its colour are entered as the arguments of the function.The
# third parameter controls whether or not to clear the display
# before displaying the number. Setting this parameter to 1
# will clear the display
#
# Author: Dogan Ibrahim
# Date  : March 2022
# File  : display.py
#------------------------------------------------------------
from sense_hat import SenseHat
sense = SenseHat()

def Disp(no, colour, mode):
#
# Number patterns for all the numbers 0 to 9
#
	numbers = [
	[[0,1,1,0], 		# 0
	[1,0,0,1],
	[1,0,0,1],
	[1,0,0,1],
	[1,0,0,1],
	[1,0,0,1],
	[1,0,0,1],
	[0,1,1,0]],

	[[0,0,1,0],		# 1
	[0,1,1,0],
	[0,0,1,0],
	[0,0,1,0],
	[0,0,1,0],
	[0,0,1,0],
	[0,0,1,0],
	[0,1,1,1]],

	[[0,1,1,0],		# 2
	[1,0,0,1],
	[0,0,0,1],
	[0,0,0,1],
	[0,0,1,0],
	[0,1,0,0],
	[1,0,0,0,],
	[1,1,1,1]],

	[[1,1,1,1],		# 3
	[0,0,1,1],
	[0,0,1,1],
	[1,1,1,1],
	[1,1,1,1],
	[0,0,1,1],
	[0,0,1,1],
	[1,1,1,1]],

	[[0,0,1,0],		# 4
	[0,1,1,0],
	[1,1,1,0],
	[1,0,1,0],
	[1,1,1,1],
	[0,0,1,0],
	[0,0,1,0],
	[0,0,1,0]],

	[[1,1,1,1],		# 5
	[1,0,0,0],
	[1,0,0,0],
	[1,1,1,1],
	[0,0,0,1],
	[0,0,0,1],
	[0,0,0,1],
	[1,1,1,1]],

	[[1,1,1,1],		# 6
	[1,0,0,0],
	[1,0,0,0],
	[1,1,1,1],
	[1,0,0,1],
	[1,0,0,1],
	[1,0,0,1],
	[1,1,1,1]],

	[[1,1,1,1],		# 7
	[0,0,0,1],
	[0,0,0,1],
	[0,0,0,1],
	[0,0,0,1],
	[0,0,0,1],
	[0,0,0,1],
	[0,0,0,1]],

	[[0,1,1,0],		# 8
	[1,0,0,1],
	[1,0,0,1],
	[1,1,1,1],
	[1,0,0,1],
	[1,0,0,1],
	[1,0,0,1],
	[0,1,1,0]],

	[[1,1,1,1],		# 9
	[1,0,0,1],
	[1,0,0,1],
	[1,1,1,1],
	[0,0,0,1],
	[0,0,0,1],
	[0,0,0,1],
	[1,1,1,1]]
	]

	blank = [0,0,0]
	blanks=[0,0,0,0]
	Disp = []				# List to store patterns

	for index in range(0, 8):
    		if (no >= 10):				# If >= 10
        		intno = int(no / 10)			# MSD digit
        		Disp.extend(numbers[intno][index])
    		else:
        		Disp.extend(blanks)
    		remno = int(no % 10)			# LSD digit
    		Disp.extend(numbers[remno][index])

	for index in range(64):
  		if(Disp[index]):
      			Disp[index]=colour		# Colour
  		else:
    			Disp[index]=blank

	if mode == 1:
           sense.clear()				# Clear LEDs

	sense.set_pixels(Disp)				# Display number

