#---------------------------------------------------------------
#               ANALOG TEMPERATURE SENSOR
#               =========================
#
# In this project a TMP36 type analog temperature chip is used
# to measure the ambient temperature. The temperature is read
# using a MCP3002 type ADC chip. The result is converted into
# degrees Centigrade and is displayed on the monitor
#
# Program: tmp36.py
# Date   : December, 2022
# Author : Dogan Ibrahim
#----------------------------------------------------------------
import RPi.GPIO as GPIO
import spidev
import time
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

#
# Start of main program. Read the analog temperature, convert
# into degrees Centigrade and display on the monitor every second
#
while True:
   adc = get_adc_data(0)
   mV = adc * 3300.0 / 1023.0			# convert to mV
   Temp = (mV - 500.0) / 10.0			# temperature in C
   print("Temperature = %5.2f " %Temp)		# display temperature
   time.sleep(1)				# wait one second
