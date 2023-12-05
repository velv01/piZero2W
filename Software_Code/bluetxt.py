#=======================================================
#		BLUETOOTH COMMUNICATION
#		=======================
#
# In this project text messages are exchanged with a smart
# phone using the Bluetooth protocol
#
# Author: Dogan Ibrahim
# File  : bluetxt.py
# Date  : December, 2022
#========================================================
import socket
import bluetooth

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
# Now receive text from smart phone and display
#
try:

   while True:
      data = ClientSock.recv(1024)			# receive text
      print("Received data: ", data.decode('utf-8'))
      msg = input("Enter data to send: ")		# TExt to send
      ClientSock.send(msg.encode('utf-8'))		# Send text

except KeyboardInterrupt:				# Keyboard int
      ServerSock.close()				# Close socket


