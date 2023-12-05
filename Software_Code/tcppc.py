#===============================================================
#	SEND/RECEIVE TEXT MESSAGES USING TCP/IP
#	=======================================
#
# This is the TCP/IP server program. It communicates with a PC
# running TCP/IP on the same port
#
# Author: Dogan Ibrahim
# File  : tcppc.py
# Date  : December, 2022
#==============================================================
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("192.168.3.21", 5000))
sock.listen(1)

client, addr = sock.accept()			# accept connection
print("Connected to client: ", addr)		# connected message

try:
   while True:
      msg = input("Enter your message: ")	# read a message
      msg = msg +"\n"
      client.send(msg.encode('utf-8'))		# send the message

      msg = client.recv(1024)
      print("Received message: ", msg.decode('utf-8'))

except KeyboardInterrupt:
      print("\nClosing connection to client")
      sock.close()
      time.sleep(1)





