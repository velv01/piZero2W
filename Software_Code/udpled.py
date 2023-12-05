#==================================================================
#	CONTROL LED FROM SMART PHONE
#	============================
#
# In this program UDP is used where Zero 2 W is the server
# and smart phone is the client. An LED connected to the server
# and is controlled from the smart phone
#
# Author: DOgan Ibrahim
# File  : udpled.py
# Date  : December, 2022
#===================================================================
import socket
import RPi.GPIO as GPIO
import time

LED = 2						# LED port
GPIO.setwarnings(False)				# No warnings
GPIO.setmode(GPIO.BCM)				# BCM numbering
GPIO.setup(LED, GPIO.OUT)			# LED is output
GPIO.output(LED, 0)				# LED OFF at start

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("192.168.3.21", 2000))		# Bind to Zero 2 W IP,port

data = [' '] * 10
while data != b'X':
  data, addr = sock.recvfrom(1024)
  if data == b'ON':				# ON command
     GPIO.output(LED, 1)			# LED ON
  elif data == b'OFF':				# OFF command
     GPIO.output(LED, 0)			# LED OFF

print("Closing connection")
GPIO.cleanup()
sock.close()
time.sleep(1)

