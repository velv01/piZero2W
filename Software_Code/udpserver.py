#=======================================================
#	SEND TEXT MESSAGES USING UDP
#	============================
#
# This is the UDP server program running on Zero 2 W.
# The program exchanges text messages with an Android
# smart phone
# 
# Author: Dogan Ibrahim
# File  : udpserver.py
# Date  : December, 2022
#=======================================================
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("192.168.3.21", 5000))

try:
  while True:
    data, addr = sock.recvfrom(1024)
    print("Received msg:", data.decode('utf-8'))
    msg = input("Message to send: ")
    sock.sendto(msg.encode('utf-8'), addr)

except KeyboardInterrupt:
  print("\nClosing connection to client")
  sock.close()



