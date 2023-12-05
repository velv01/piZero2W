#---------------------------------------
#
#      LCD TEST PROGRAM
#      ================
#
# Author: Dogan Ibrahim
# File  : lcdtest.py
# Date  : December, 2022
#---------------------------------------
from RPLCD.i2c import CharLCD
lcd=CharLCD('PCF8574', 0x27)

lcd.clear()
lcd.home
lcd.write_string("MY LCD")


