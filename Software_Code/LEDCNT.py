#-----------------------------------------------------------
#
#               BINARY UP COUNTING LEDs
#               =======================
#
# In this project 8 LEDs are connected to the following
# GPIO pins:
#
# 9 10 22 27 17 4 3 2
# 
# The program groups these LEDs as an 8-bit port and then
# the LEDs count up in binary with one second delay between
# each output.
#
# Program: LEDCNT.py
# Date   : December, 2022
# Author : Dogan Ibrahim
#------------------------------------------------------------
import RPi.GPIO as GPIO			# import GPIO library
import time				# import time library
GPIO.setwarnings(False)			# disable warning messages
GPIO.setmode(GPIO.BCM)			# set BCM pin numbering
PORT = [9, 10, 22, 27, 17,  4,  3,  2]	# port connections
DIR = ["0","0","0","0","0","0","0","0"]	# port directons

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
# Main program loop. Count up in binary every second
#
cnt = 0
while True:
  Port_Output(cnt)			# send cnt to port
  time.sleep(1)				# wait 1 second
  cnt = cnt + 1				# increment cnt


