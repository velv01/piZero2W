#--------------------------------------------------------------
#		FLASHING AN EXTERNAL LED
#		========================
#
# In this program an external LED is connected to port pin GPIO2
# (pin 3). The LED is flashed every second.
#
# This program detects CNTRL+C and terminates orderly
#
# Author: Dogan Ibrahim
# File  : ExtFlash2.py
# Date  : December, 2022
#----------------------------------------------------------------
import RPi.GPIO as GPIO			# import GPIO library
import time				# import time library
GPIO.setmode(GPIO.BCM)			# set BCM pin numbering

LED = 2					# LED at port GPIO2
ON = 1					# ON = 1
OFF = 0					# OFF = 0
GPIO.setup(LED, GPIO.OUT)		# configure LED as output

try:

   while True:				# DO FOREVER
        GPIO.output(LED, ON)		# turn ON LED
        time.sleep(1)			# wait 1 second
        GPIO.output(LED, OFF)		# turn OFF LED
        time.sleep(1)			# wait 1 second

except KeyboardInterrupt:		# CNTRL+C detected
        GPIO.output(LED, 0)		# set LED OFF
        GPIO.cleanup()			# clear GPIO buffers
 
