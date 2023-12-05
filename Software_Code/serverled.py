#=============================================================
#	CONTROL LED FROM SMART PHONE
#	============================
#
# In this program TCP/IP is used where Zero 2 W is the server
# and smart phone is the client. An LED connected to Zero 2 W
# GPIO 2 and is controlled from the smart phone
#
# Author: DOgan Ibrahim
# File  : serverled.py
# Date  : December, 2022
#===============================================================
import socket
import RPi.GPIO as GPIO
import time

LED = 2					# LED port
GPIO.setwarnings(False)			# No warnings
GPIO.setmode(GPIO.BCM)			# BCM numbering
GPIO.setup(LED, GPIO.OUT)		# LED is output
GPIO.output(LED, 0)			# LED OFF

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("192.168.3.21", 5000))       # Zero 2 W IP, port
sock.listen(1)
client, addr = sock.accept()
print("Connected")

data = [' '] * 10


while data != b'X\n':			# Terminate?
  data = client.recv(1024)
  if data == b'ON\n':			# ON
     GPIO.output(LED, 1)
  elif data == b'OFF\n':		# OFF
     GPIO.output(LED, 0)

print("Closing connection")
GPIO.cleanup()
sock.close()
time.sleep(1)

