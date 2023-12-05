#--------------------------------------------------------------
#		LUCKY DAY OF THE WEEK
#		=====================
#
# In this program 7 LEDs are connected to Zero 2 W where each
# LED represents a day of the week. Pressing a button
# turns ON one of the LEDs randomly and this corresponds to
# your lucky day of the week
#
# Author: Dogan Ibrahim
# File  : LuckyDay.py
# Date  : December, 2022
#---------------------------------------------------------------
import RPi.GPIO as GPIO			# import GPIO library
import time				# import time library
GPIO.setwarnings(False)			# disable warning messages
GPIO.setmode(GPIO.BCM)			# set BCM pin numbering
import random				# random no
from datetime import datetime

PORT = [9, 10, 22, 27, 17,  4,  3,  2]	# port connections
DIR = ["0","0","0","0","0","0","0","0"]	# port directons
BUTTON = 11
GPIO.setup(BUTTON, GPIO.IN)

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
# Configure PORT to all outputs
#
Configure_Port()

#
# Main program loop, check if Button is pressed
#
print("Press the Button to display your lucky number...")
dt = datetime.today()
seconds = dt.timestamp()
random.seed(seconds)

while GPIO.input(BUTTON) == 1:		# If Button not pressed
   pass

r = random.randint(1, 7)		# Generate random number
r = pow(2, r-1)				# LED to be turned ON
Port_Output(r)			        # Send to LEDs


 
