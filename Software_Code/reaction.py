#----------------------------------------------------------
#                 REACTION TIMER
#                 ==============
#
# This is a reaction timer program. The user presses a button
# as soon as he/she see a light. The time between seeing the
# light and pressing the button is measured and is displayed
# in milliseconds as the reaction time of the user. The light
# comes ON after a random number of seconds between 1 and 10
# seconds.
#
# Program: reaction.py
# Date   : December, 2022
# Author : Dogan Ibrahim
#-----------------------------------------------------------
import RPi.GPIO as GPIO
import time
import random

LED = 2					# LED at GPIO 2
Button = 3				# Button at GPIO 3

GPIO.setwarnings(False)			# Disable warnings
GPIO.setmode(GPIO.BCM)			# BCM mode

#
# LED is output, button is input
#
GPIO.setup(Button, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED, 0)			# LED OFF to start with

#
# Start of main program
#
while True:
   T = random.randint(1, 10)
   time.sleep(T)
   GPIO.output(LED, 1)
   start_time = time.time()		# start time
   while (GPIO.input(Button) == 1):	# wait until button pressed
      pass
   end_time = time.time()
   diff_time = 1000.0*(end_time - start_time)
   diff_int = int(diff_time)
   print("Reaction time=%d " %diff_int)
   GPIO.output(LED, 0)
   time.sleep(3)

   



