#---------------------------------------------------------
#             I2C LCD SECONDS COUNTER
#             =======================
#
# In this program an I2C LCD is connected to the Zero 2 W.
# The program counts up in seconds and displays on the LCD.
#
# At the beginning of the program the text SECONDS COUNTER is
# displayed for 2 seconds
#
# Program: lcd.py
# Date   : December, 2022
# Author : Dogan Ibrahim
#----------------------------------------------------------
import time
from RPLCD.i2c import CharLCD
lcd=CharLCD('PCF8574', 0x27)			# Init LCD

lcd.clear()					# clear LCD
lcd.write_string("SECONDS COUNTER")		# display string
time.sleep(2)					# wait 2 seconds

cnt = 0						# initialize cnt
lcd.clear()					# clear lcd

while True:					# infinite loop
  cnt = cnt + 1					# increment count
  lcd.cursor_pos = (0, 0)			# Top row
  lcd.write_string(str(cnt))			# display cnt
  time.sleep(1)					# wait one second

