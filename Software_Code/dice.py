#------------------------------------------------------------------
#
#                    ELECTRONIC DICE
#                    ===============
#
# This program is an electronic dice. GPIO 11 of Zero 2 W is
# configured as an input and a push-button switch is connected to
# this port pin. When the button is pressed a random dice number is
# displayed between 1 and 6 on the LEDs.
#
# 7 LEDs are mounted on the breadboard in the form of the face of
# a real dice. The following GPIO pins are used for the LEDs (bit
# 7 is mot used):
#
#  Port pin: 7  6  5  4  3 2 1 0
#  GPIO    :   10 22 27 17 4 3 2
#
# The following PORT pins are used to construct the dice:
#
# D0    D4
# D1 D3 D5
# D2    D6
#
# Program: dice.py
# Date   : December, 2022
# Author : Dogan Ibrahim
#------------------------------------------------------------------
import RPi.GPIO as GPIO			# import GPIO library
import time				# import time library
import random				# import random library
GPIO.setwarnings(False)

PORT = [9, 10, 22, 27, 17, 4, 3, 2]

DICE_NO = [0, 0x08, 0x41, 0x49, 0x55, 0x5D, 0x77]

#
# This function configures the port directions
#
def Configure_Port():
   for i in range (0, 8):
         GPIO.setup(PORT[i], GPIO.OUT)
   return

#
# This function sends a byte (8-bit) data to the PORT
#
def Port_Output(x):
   b = bin(x)				# convert into binary
   b = b.replace("0b", "")		# remove leading 0b
   diff = 8 - len(b)			# find the difference
   for i in range (0, diff):
      b = "0" + b			# insert leading 0s

   for i in range (0, 8):
      if b[i] == "1":
         GPIO.output(PORT[i], 1)
      else:
         GPIO.output(PORT[i], 0)
   return

#
# The program jumps here after the button is pressed
#
def DICE(dummy):
   n = random.randint(1, 6)		# generate a random number
   pattern = DICE_NO[n]			# find the pattern
   Port_Output(pattern)			# turn ON required LEDs
   time.sleep(3)			# wait for 3 seconds
   Port_Output(0)			# turn OFF all LEDs
   return

#
# Start of main program
#
Dice_Pin = 11
GPIO.setmode(GPIO.BCM)

GPIO.setup(Dice_Pin, GPIO.IN)
#
# Configure PORT as outputs
#
Configure_Port()
#
# Setup callback to function DICE when the button is pressed
#
GPIO.add_event_detect(Dice_Pin, GPIO.FALLING, bouncetime=50,
                      callback=DICE)
#
# Program waits here for the button to be pressed, then a random
# number is generated between 1 and 6 and is displayed on the LEDs
#
while True:
   pass						# Do nothing



