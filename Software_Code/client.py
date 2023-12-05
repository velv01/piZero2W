#=============================================================
#               TCP/IP CLIENT
#               =============
#
# This is the client program on the PC.The program exchanges
# messages with the server on the Raspberry Pi Zero 2 W
#
# Author: Dogan Ibrahim
# File  : client.py
# Date  : December 2022
#=============================================================
import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.connect(("192.168.3.21", 5000))

try:
    while True:
        msg = sock.recv(1024)
        print("Received message: ", msg.decode('utf-8'))
        data = input("Enter message to send: ")
        sock.send(data.encode('utf-8'))

except KeyboardInterrupt:
    print("Closing connection to server")
    sock.close()
    time.sleep(1)


