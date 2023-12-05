#-----------------------------------------------------------------
#		        Times Table
#                       -----------
#
# This program generates a times table. The table is selected at the
# beginning of the program by setting variable Tablefor.
#
# Author: Dogan Ibrahim
# File  : timestab.py
# Date  : December, 2022
#-------------------------------------------------------------------
from sense_hat import SenseHat
sense = SenseHat()
import time

spd = 0.2						# Scroll speed
red = (255, 0, 0)					# Red colour
Tablefor = 5						# Table for 5

try:

  for k in range(12):					# Do 0 to 11
    j = k + 1						# 1 to 12
    result = Tablefor * j
    disp = str(Tablefor) + "x" + str(j) + "=" + str(result) 
    sense.show_message(disp, scroll_speed = spd, text_colour=(red))
    time.sleep(1)
    sense.clear()

except KeyboardInterrupt:
    exit()






