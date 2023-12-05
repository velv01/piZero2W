#----------------------------------------------------------
#	RASPBERRY PI PICO W - RASPBERRY PI ZERO 2 W COMMS
#	=================================================
#
# In this project a pushbutton is connected to GP2 of PICO W.
# Presingthe button sends a command to Zero 2 W to activate
# a relay. UDP protocol is used in this project
#
# Author: Dogan Ibrahim
# File  : picoudp.py
# Date  : December, 2022
#------------------------------------------------------------
from machine import Pin
import network
import socket
import utime
global wlan

BUTTON = Pin(2, Pin.IN)						# Button at GP2

#
# This function attempts to connect to Wi-Fi
#
def connect():
    global wlan
    wlan = network.WLAN(network.STA_IF)
    while wlan.isconnected() == False:
       print("Waiting to be connected")
       wlan.active(True)
       wlan.connect("TP-Link_6138_EXT", "24844604")
       utime.sleep(5)

connect()
print("Connected")
UDP_PORT = 2000								# Port used
UDP_IP = "192.168.3.21"						# Zero 2W IP
cmd = b"1"									# Cmd to turn ON
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    while BUTTON.value() == 1:				# Not pressed
       pass
    while BUTTON.value() == 0:				# Not released
       pass
    sock.sendto(cmd, (UDP_IP, UDP_PORT))	# Send cmd
    print("Command sent")					# Message
    utime.sleep(1)							# Wait 1 sec
   

