#=======================================================
#		LED CONTROL BY BLUETOOTH
#		========================
#
# In this project an LED is connected to GPIO 17.The LED
# LED is controlled by sending commands from an Android
# smart phone using a Bluetooth apps.
#
# Valid comamdns are:
# L1 Turn ON the LED
# L0 Turn OFF the LED
#
# Author: Dogan Ibrahim
# File  : blueled.py
# Date  : December, 2022
#========================================================
import socket
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
import bluetooth

#
# LED is at GPIO 17, configure as output and turn OFF
#
LED = 17				# LED at port 17
GPIO.setup(LED, GPIO.OUT)			# LED as output
GPIO.output(LED, 0)				# LED OFF

#
# Start of main program loop.Configure Bluetooth, create a
# port, listen for client connections, and accept connection
#
port = 1
ServerSock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
ServerSock.bind(("", port))
ServerSock.listen(1)
ClientSock, addr = ServerSock.accept()

#
# Now receive comamnds and decode
#
try:

   while True:
     data = ClientSock.recv(1024)		# receive command
     if data == b'L1\r\n':			# L1?
         GPIO.output(LED, 1)			# turn ON LED
     elif data == b'L0\r\n':			# L0?
          GPIO.output(LED, 0)			# turn OFF LED

except KeyboardInterrupt:			# Interrupt
     ServerSock.close()
