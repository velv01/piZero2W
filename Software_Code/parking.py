#-------------------------------------------------------------------
#                         PARKING SENSORS
#                         ===============
#
# This is a parking sensors project. Ultrasonic tranamitter/receiver
# sensors are attached to the front and rear of a vehicle. In addition
# an active buzzer is connected to the Zero 2 W. The program senses
# the objects in the front and rear of the vehicle and sounds the buzzer
# if the vehicle is too close to the objects. In this project a distance
# less than 10cm is considered to be too close. 
#
# File  : parking.py
# Date  : December, 2022
# Author: Dogan Ibrahim
#--------------------------------------------------------------------
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
Allowed_Distance = 10			# Distance in cm

#
# Front Ultrasonic sensor pins
#
trig_f = 2				# GPIO 2
echo_f = 3				# GPIO 3

#
# Rear ultrasonic sensor pins
#
trig_r = 4				# GPIO 4
echo_r = 17				# GPIO 17

#
# BUZZER pin
#
Buzzer = 27				# GPIO 27

#
# Configure trig and buzzer as outputs, echos as inputs
#
GPIO.setup(trig_f, GPIO.OUT)
GPIO.setup(trig_r, GPIO.OUT)
GPIO.setup(echo_f, GPIO.IN)
GPIO.setup(echo_r, GPIO.IN)
GPIO.setup(Buzzer, GPIO.OUT)

#
# Turn ON the Buzzer
#
def BUZZERON():
  GPIO.output(Buzzer, 1)
  return

#
# Turn OFF the Buzzer
#
def BUZZEROFF():
  GPIO.output(Buzzer, 0)
  return

def GetDistance(trig, echo):
  GPIO.output(trig, 0)				# Wait to settle
  time.sleep(0.08)
  GPIO.output(trig,1)				# Send trig
  time.sleep(0.00001)				# Wait 10 microseconds
  GPIO.output(trig, 0)				# Remove trig
  while GPIO.input(echo) == 0:			# Wait until echo is received
    start_time = time.time()			# Start time

  while GPIO.input(echo) == 1:			# Echo is received
    end_time = time.time()			# End time

  pulse_width = end_time - start_time		# Pulse duration
  distance = pulse_width * 17150		# Distance in cm
  return distance				# Return distance

#
# Start of the main program loop. Measure the distance to obstacles
# at the front and rear of the vehicle and activate the buzzer if the
# distance is below the allowed distance
#
BUZZEROFF()

while True:
  obstacle_f = GetDistance(trig_f, echo_f)	# distance to front obstacles
  obstacle_r = GetDistance(trig_r, echo_r)	# distance to rear obstacles
  if (obstacle_f <= Allowed_Distance or obstacle_r <= Allowed_Distance):
    BUZZERON()					# Turn Buzzer ON
  else:
    BUZZEROFF()					# Turn Buzzer OFF
  




