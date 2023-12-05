#---------------------------------------------------------
#		FLASHING AN EXTERNAL LED
#		========================
#
# In this program an external LED is connected to port pin
# GPIO2 (pin 3). The LED is flashed every second
#
# Author: Dogan Ibrahim
# File  : ExtFlash.py
# Date  : December, 2022
#----------------------------------------------------------
import RPi.GPIO as GPIO		# import GPIO library
import time			# import time library
GPIO.setwarnings(False)		# disable warning messages
GPIO.setmode(GPIO.BCM)		# set BCM pin numbering

LED = 2				# LED at port GPIO2
ON = 1				# ON = 1
OFF = 0				# OFF = 0
GPIO.setup(LED, GPIO.OUT)	# configure LED as output

while True:
  GPIO.output(LED, ON)		# turn ON LED
  time.sleep(1)			# wait 1 second
  GPIO.output(LED, OFF)		# turn OFF LED
  time.sleep(1)			# wait 1 second


    