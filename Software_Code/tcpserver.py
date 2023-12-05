#===============================================================
#	SEND TEXT MESSAGES USING TCP/IP
#	===============================
#
# This is the TCP/IP server program. It receives text messages
# from the keyboard and sends to an Android smart phone over 
# a Wi-Fi link
#
# Author: Dogan Ibrahim
# File  : tcpserver.py
# Date  : December, 2022
#==============================================================
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("192.168.3.21", 5000))
sock.listen(1)

client, addr = sock.accept()			# accept connection
print("Connected to client: ", addr)		# connected message

yn = 'y'

while yn == 'y':
  msg = input("Enter your message: ")		# read a message
  client.send(msg.encode('utf-8'))		# send the message

  yn = input("Send more messages?: ")
  yn = yn.lower()

print("\nClosing connection to client")
sock.close()




