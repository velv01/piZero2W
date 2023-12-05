#---------------------------------------------------------------
#               ANALOG TEMPERATURE SENSOR - LCD OUTPUT
#               ======================================
#
# In this project a TMP36 type analog temperature chip is used
# to measure the ambient temperature. The temperature is read
# using a MCP3002 type ADC chip. The result is converted into
# degrees Centigrade and is displayed on I2C LCD
#
# Program: tmp36lcd.py
# Date   : December, 2022
# Author : Dogan Ibrahim
#----------------------------------------------------------------
import RPi.GPIO as GPIO
import spidev
import time
from RPLCD.i2c import CharLCD
lcd=CharLCD('PCF8574', 0x27)
GPIO.setwarnings(False)

#
# Create SPI instance and open the SPI bus
#
spi = spidev.SpiDev()
spi.open(0,0)				# we are using CE0 for CS
spi.max_speed_hz = 4000

GPIO.setmode(GPIO.BCM)

#
# This function returns the ADC data read from the MCP3002
#
def get_adc_data(channel_no):
   ADC = spi.xfer2([1, (2 + channel_no) << 6, 0])
   rcv = ((ADC[1] & 15) << 6) + (ADC[2] >> 2)
   return rcv

lcd.clear()
lcd.home()
lcd.write_string("TEMP - TMP36")
time.sleep(2)

#
# Start of main program. Read the analog temperature, convert
# into degrees Centigrade and display on the monitor every second
#
while True:
   adc = get_adc_data(0)
   lcd.clear()
   lcd.home()
   lcd.write_string("Temperature")		# heading
   lcd.cursor_pos = (1, 0)			# cursor at (1, 0)
   mV = adc * 3300.0 / 1023.0			# convert to mV
   Temp = (mV - 500.0) / 10.0			# temperature in C
   T = str(Temp)[:5]
   lcd.write_string(T)				# display temperature
   time.sleep(2)				# wait two seconds
