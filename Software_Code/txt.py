#-----------------------------------------------------------
#		           Display Text
#                          ------------
#
# This program displays the text Sense HAT every 2 seconds.
# the text colour is RED and back ground colour is YELLOW
#
# Author: Dogan Ibrahim
# File  : txt.py
# Date  : December, 20202
#------------------------------------------------------------
from sense_hat import SenseHat
import time
sense = SenseHat()

while True:
   sense.show_message("Sense HAT",scroll_speed=0.3,\
text_colour=[255,0,0],back_colour=[255,255,0])
   time.sleep(2)


