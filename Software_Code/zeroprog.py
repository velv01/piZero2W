#=======================================================
#		RELAY CONTROL BY BLUETOOTH
#		==========================
#
# In this Case Study a Relay is connected to GPIO 4.The
# Relay is controlled by sending command from an Arduino
# Uno using a Bluetooth apps.
#
# Valid command is: "1"
#
# Author: Dogan Ibrahim
# File  : zeroprog.py
# Date  : December, 2022
#========================================================
import RPi.GPIO as GPIO
import serial
import time
GPIO.setmode(GPIO.BCM)

#
# Relay is on GPIO 2, configure as output and turn OFF
#
RELAY = 4				# Relay at port 4
GPIO.setup(RELAY, GPIO.OUT)		# Relay as output
GPIO.output(RELAY, 0)			# Relay OFF

#
# Attach to virtual serial port /dev/rfcomm0
#
ser = serial.Serial(port='/dev/rfcomm0', baudrate=9600)

#
# Now receive commands and decode
#
try:

   while True:
     data = ser.read()			# receive comman
     if data == b'1':			# 1?
         GPIO.output(RELAY, 1)		# activate Relay
         time.sleep(5)			# 5 seconds
         GPIO.output(RELAY, 0)		# Relay OFF

except KeyboardInterrupt:		# Interrupt
     GPIO.output(RELAY, 0)		# deactivate Relay
     GPIO.cleanup()
