#--------------------------------------------------------------------
#		ON-OFF TEMPERATURE CONTROLLER
#		-----------------------------
#
# This is an ON-OFF temperature control project. In this project
# a buzzer is connected to port pin GPIO 4 of the Zero 2 W in
# addition to the Sense HAT. The Sense HAT is connected using
# jumper wires. The buzzer is turned ON if the ambient temperature
# is below the setpoint temperature. At the same time, the ambient
# temperature is displayed in red colour. If on the other hand the
# ambient temperature is higher than the setpoint value then the
# buzzer is turned OFF and the display is in blue colour.
#
# The buzzer in this program can be replaced with a relay for
# example to control a heater
#
# Author: Dogan Ibrahim
# Date  : December, 2022
# File  : tempcont.py
#--------------------------------------------------------------------
from display import Disp				# import Disp
from sense_hat import SenseHat				# import Sense HAT
sense=SenseHat()
import time						# import time
import RPi.GPIO as GPIO					# import GPIO

GPIO.setwarnings(False)					# disable warnings
GPIO.setmode(GPIO.BCM)					# set GPIO mode

Buzzer = 4						# Buzzer at GPIO4
SetTemperature = 24					# setpoint temp
red = (255, 0 ,0)					# red colour
blue = (0, 0, 255)					# blue colour

GPIO.setup(Buzzer, GPIO.OUT)				# Buzzer is output
GPIO.output(Buzzer, 0)					# Buzzer OFF

while True:
   T = int(sense.get_temperature_from_humidity())	# get temperature
   if(T < SetTemperature):				# T < setpoint?
      Disp(T, red, 0)					# display in red
      GPIO.output(Buzzer, 1)				# Buzzer ON
   else:
      Disp(T, blue, 0)					# display in blue
      GPIO.output(Buzzer, 0)				# Buzzer OFF

   time.sleep(5)					# wait 5 secs


