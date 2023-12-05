#=========================================================
#	RASPBERRY PI PICO W - RASPBERRY PI ZERO 2 W COMMS
#	============================
#
# This is the UDP server program running on Zero 2 W. The
# program receives a command from PICO W and activates a
# relay connected to GPIO 2 for 5 seconds
# 
# Author: Dogan Ibrahim
# File  : zeroudp.py
# Date  : December, 2022
#=======================================================
import RPi.GPIO as GPIO
GPIO.setwarnings (False)
GPIO.setmode(GPIO.BCM)
import socket
import time

RELAY = 2				# Relay at port 2
GPIO.setup(RELAY, GPIO.OUT)		# Relay is output
GPIO.output(RELAY, 0)			# Deenergize Relay

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("192.168.3.21", 2000))

try:
  while True:
    data, addr = sock.recvfrom(1024)	# GEt command
    if data == b'1':			# Command is 1?
       GPIO.output(RELAY, 1)		# Activate Relay
       time.sleep(5)			# 5 seconds delay
       GPIO.output(RELAY, 0)		# Deactivate Relay

except KeyboardInterrupt:		# Keyboard interrupt
  print("\nClosing connection to client")
  sock.close()



