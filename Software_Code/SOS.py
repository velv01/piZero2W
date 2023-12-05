#---------------------------------------------------------
#			LED FLASHING SOS
#			================
#
# In this program the external LED at port GPIO2 flashes the
# SOS signal (... --- ...)
#
# Author: Dogan Ibrahim
# File  : SOS.py
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

Dot = 0.25                      # Dot time
Dash = 1.0                      # Dash time
Gap = 0.2                       # Gap time

while True:			# DO FOREVER
    for i in range(0, 3):
        GPIO.output(LED, ON)
        time.sleep(Dot)        	# Wait Dot time
        GPIO.output(LED, OFF)  	# LED OFF
        time.sleep(Gap)        	# Wait Gap time
        
    time.sleep(0.5)            	# 0.5 second delay
    
    for i in range(0, 3):
        GPIO.output(LED, ON)    # LED ON
        time.sleep(Dash)       	# Wait Dash time
        GPIO.output(LED, OFF)  	# LED OFF
        time.sleep(Gap)       	# Wait Gap time
        
    time.sleep(0.5)		# 0.5 second delay
        
    for i in range(0, 3):
        GPIO.output(LED, ON)    # LED ON
        time.sleep(Dot)        	# Wait Dot time
        GPIO.output(LED, OFF)   # LED OFF
        time.sleep(Gap)        	# Wait Gap time
    
    time.sleep(2)              # Wait 2 seconds


