#-----------------------------------------------------------------------------
#        ATMOSPHERIC PRESSURE AND TEMPERATURE ON THE CLOUD
#	 =================================================
#
# The ambient temperature and pressure sensor BMP280 is connected to Zero 2 W.
# The project reads the temperature and atmospheric pressure and sends
# to the Cloud where it can be accessed from anywhere. In addition, change
# of the temperature and the pressure can be plotted in the cloud.
#
#
# The program uses the Thingspeak cloud service
#
# Author: Dogan Ibrahim
# File  : Cloud.py
# Date  : January, 2022
#------------------------------------------------------------------------------
import socket
import time
from bmp280 import BMP280
from smbus import SMBus

bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

APIKEY = "2TE7WHRAWTWKGXZ4"                    # Thingspeak API key
host = "api.thingspeak.com"                    # Thigspeak host

#
# Send data to Thingspeak. This function sends the temperature and
# humidity data to the cloud every 30 seconds
#
while True:
   sock = socket.socket()
   addr = socket.getaddrinfo("api.thingspeak.com",80)[0][-1] 
   sock.connect(addr)
   p=bmp280.get_pressure()
   t=bmp280.get_temperature()                  # Temperature in C
   path = "api_key="+APIKEY+"&field1="+str(p)+"&field2="+str(t)  
   sock.send(bytes("GET /update?%s HTTP/1.0\r\nHost: %s\r\n\r\n" %(path,host),"utf8"))
   time.sleep(5)
   sock.close()
   time.sleep(25)

