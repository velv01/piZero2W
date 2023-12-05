#--------------------------------------------------------------
#		TEMPERATURE,HUMIDITY & PRESSURE
#		-------------------------------
#
# This program reads the temperature, humidity and pressure and
# displays on the scrolling LEDs. The data is displayed in the
# following format:
#
#  T=nn.nC H=nn.n% P=nnnn.nmb
#
# Author: Dogan Ibrahim
# Date  : December, 2022
# File  : thp.py
#--------------------------------------------------------------
from sense_hat import SenseHat
sense=SenseHat()
import time

while True:
   T = round(sense.get_temperature(), 1)	# Get temperature
   H = round(sense.get_humidity(), 1)		# Get humidity
   P = round(sense.get_pressure(), 1)		# Get pressure
   enviro = "T="+str(T)+ "C H="+str(H)+ "% P="+str(P)+"mb "
   sense.show_message(enviro, scroll_speed = 0.2)
   time.sleep(2)


