#----------------------------------------------------------
#				DISPLAY A CUSTOM CHARACTER
#				==========================
#
# This program displays an arrow character on the LCD
#
# Author: Dogan Ibrahim
# File  : arrow.py
# Date  : October 2022
#------------------------------------------------------------
import machine
from machine import I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import utime

I2C_ADDR = 0x27                   # I2C LCD address
NRows = 2                         # Number of rows
NColumns = 16                     # Number of columns

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, NRows, NColumns)

arrow = bytearray([0x04,0x0E,0x15,0x04,0x04,0x04,0x04,0x04])
lcd.custom_char(0, arrow)
lcd.putstr(chr(0))

    

