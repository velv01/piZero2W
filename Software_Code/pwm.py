#-----------------------------------------------------------------------
#               LED BRIGHTNESS CONTROL
#               ======================
#
# In this program two buttons and an LED are used. Pressing button
# BRIGHTER makes the LED brighter. Simialrly, pressing button DIMMER
# makes the LED dimmer. PWM waveform is used to drive the LED where
# the Duty Cycle is changed (increased or decreased by 5) each time 
# a button is pressed. PWM frequency is set to 200 Hz
#
# File  : pwm.py
# Date  : December, 2022
# Author: Dogan Ibrahim
#-------------------------------------------------------------------------
import RPi.GPIO as GPIO			# import GPIO module
GPIO.setwarnings(False)
import time

GPIO.setmode(GPIO.BCM)
BRIGHTER = 2				# button BRIGHTER
DIMMER = 3				# button DIMMER
LED = 4					# LED

GPIO.setup(LED, GPIO.OUT)		# configure LED output
GPIO.setup(BRIGHTER, GPIO.IN)		# configure BRIGHTER input
GPIO.setup(DIMMER, GPIO.IN)		# configure DIMMER input

p = GPIO.PWM(LED, 200)			# generate PWM waveform
Duty = 50				# Initial Duty Cycle
p.start(Duty)				# set duty cycle to 50%

while True:				# wait here
   p.ChangeDutyCycle(Duty)		# set/change Duty Cycle
   if GPIO.input(BRIGHTER) == 0:	# if BRIGHTER pressed
       if Duty < 100:			# if not max Duty Cycle
          Duty = Duty + 5		# increase Duty Cycle
          time.sleep(0.25)		# wait a bit
       else:
          Duty = 100			# set to max Duty Cycle

   elif GPIO.input(DIMMER) == 0:	# if DIMMER is pressed
       if Duty > 0:
          Duty = Duty - 5		# decrease Duty Cycle
          time.sleep(0.25)		# wait a bit
       else:
          Duty = 0			# set to min Duty Cycle


