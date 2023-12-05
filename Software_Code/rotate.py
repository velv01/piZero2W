#------------------------------------------------------------------
#
#               ROTATING LEDs WITH PUSH-BUTTON
#               ==============================
#
# In this project 8 LEDs are connected to the Raspberry Pi 3.
# In addition, a push-button switch is connected to GPIO 11
# (pin 23) through resistors. Normally the output of the button
# is at logic 1 and goes to logic 0 when the button is pressed.
# The LEds rotate in one direction when the button is not pressed
# and in the opposite direction when the button is pressed.
#
# Connections of the LEDs are to the following GPIO pins:
#
# 9 10 22 27 17 4 3 2
# 
# On second delay is inserted between each output.
#
# Program: rotate.py
# Date   : December, 2022
# Author : Dogan Ibrahim
#--------------------------------------------------------------------
import RPi.GPIO as GPIO				# import GPIO library
import time					# import time library
GPIO.setwarnings(False)				# disable warning messages
GPIO.setmode(GPIO.BCM)				# set BCM pin numbering
PORT = [9, 10, 22, 27, 17,  4,  3,  2]		# port connections
DIR =  ["0","0","0","0","0","0","0","0"]	# port directions
GPIO.setup(11, GPIO.IN)				# GPIO 11 is input

#
# This function configures the port pins as outputs ("0") or
# as inputs ("I")
#
def Configure_Port():
   for i in range(0, 8):
      if DIR[i] == "0":
         GPIO.setup(PORT[i], GPIO.OUT)
      else:
         GPIO.setup(PORT[i], GPIO.IN)
   return

#
# This function sends 8-bit data (0 to 255) to the PORT
#
def Port_Output(x):
   b = bin(x)				# convert into binary
   b = b.replace("0b", "")		# remove leading "0b"
   diff = 8 - len(b)			# find the length
   for i in range (0, diff):
      b = "0" + b			# insert leading os

   for i in range (0, 8):
      if b[i] == "1":
         GPIO.output(PORT[i], 1)
      else:
         GPIO.output(PORT[i], 0)
   return
#
# Configure PORT 
#
Configure_Port()

#
# Main program loop. Rotate the LEDs
#
rot = 1
while True:
  Port_Output(rot)
  time.sleep(1)				# wait 1 second
  if GPIO.input(11) == 0:		# button pressed?
    rot = rot << 1			# shift left
    if rot > 128:			# at the end
      rot = 1				# back to beginning
  else:					# button not pressed
    rot = rot >> 1			# shift right
    if rot == 0:			# at the end
      rot = 128				# back to beginning
 


 


