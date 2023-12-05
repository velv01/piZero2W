#========================================================
#		CONTROLLING LED FROM WEB PAGE
#		=============================
#
# This program turns the LED ON or OFF from a web browser
# activated from any computer on the same Wi-Fi router as
# the Zero 2 W. The commands are (assuming that the IP
# address of Raspberry Pi is: 192.168.3.21):
#
# 192.168.1.202/LED/on		turn LED ON
# 192.168.1.202/LED/off		turn LED OFF
#
# Author: Dogan Ibrahim
# File  : flasktest2.py
# Date  : December, 2022
#========================================================= 
from flask import Flask,render_template
import RPi.GPIO as GPIO

app=Flask(__name__)

#
# Define GPIO2 as output and turn OFF LED at beginning
#
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED = 2
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, 0)
  
@app.route("/<device>/<action>")
def action(device, action):
  if device == "LED":
    actuator = LED

  if action == "on":
    GPIO.output(actuator, GPIO.HIGH)
    return "LED turned ON"
  if action == "off":
    GPIO.output(actuator, GPIO.LOW)
    return "LED turned OFF"
 
if __name__ == '__main__':
   app.run(debug=True, port=80,host='0.0.0.0')

