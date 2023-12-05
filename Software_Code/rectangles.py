#-----------------------------------------------------
#	  	TWO CONCENTRIC RECTANGLES
#	  	=========================
#
# This program draws two red colour concentric rectangles
#
# Author: Dogan Ibrahim
# File  : rectangles.py
# Date  : October, 2022
#------------------------------------------------------
from ST7735 import TFT
from sysfont import sysfont
from machine import SPI, Pin

spi = SPI(0, baudrate=20000000, polarity=0, phase=0,
sck=Pin(2), mosi=Pin(3), miso=Pin(4))

tft = TFT(spi, 15, 14, 5)
tft.initg()
tft.rgb(True)

tft.fill(TFT.BLACK)							# Clear screen

tft.rect((10, 10), (110, 140), TFT.RED)		# Hollow rect
tft.rect((20, 20), (90, 120), TFT.RED)		# Hollow rect









