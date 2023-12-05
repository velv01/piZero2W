#-----------------------------------------------------------
#		        Multiplication Test
#                       -------------------
#
# This program displays two numbers between 1 and 99 and waits
# for 10 seconds until the user finds the correct answer. The
# correct answer is then displayed so that the user can check with
# his/her answer
#
# Author: Dogan Ibrahim
# File  : mult.py
# Date  : December, 2022
#------------------------------------------------------------
from sense_hat import SenseHat
sense = SenseHat()
import time
import random
spd = 0.2					# Scroll speed
red = (255, 0, 0)				# Red colour
green = (0, 255, 0)				# Green colour

try:

  while True:
    no1 = random.randint(1,99)			# First number
    no2 = random.randint(1, 99)			# Second number
    question = str(no1) + "x" + str(no2) + "="
    sense.show_message(question, scroll_speed = spd, text_colour=(green))
    time.sleep(10)
    result = str(no1 * no2)
    sense.show_message(result, scroll_speed = spd, text_colour=(red))
    time.sleep(2)
    sense.clear()
    time.sleep(1)

except KeyboardInterrupt:
    exit()






