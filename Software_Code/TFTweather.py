#=======================================================
#     DISPLAY LONDON WEATHER IN REAL-TIME ON TFT
#
# This program fetches the real-time weather data
# for a give city from Open Weather MAp and displays
# on the screen every 5 seconds
#
# Author: Dogan Ibrahim
# File  : TFTweather.py
# Date  : January, 2023
#=======================================================
from pyowm import OWM		# import Open Weather Map
import time			# import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import ST7735
from datetime import datetime

#
# Enter your API key below
#
weather = OWM('05ff9a8a5d66e4f3115c50d YOUR API')
manager = weather.weather_manager()

#
# TFT configuration
#
disp=ST7735.ST7735(port=0,cs=0,rst=27,dc=17,width=128,height=160,
rotation=90,invert=False,offset_left=0,offset_top=0)

disp.begin()
width=disp.width
height=disp.height

while True:
  img = Image.new('RGB', (160, 128), color=(0, 0, 0))
  draw = ImageDraw.Draw(img)
  font = ImageFont.load_default()

  draw.rectangle((3, 3, 150, 124), outline = (0, 0, 255))
  draw.rectangle((6, 8, 147, 120), outline = (0, 0, 255))

  draw.text((30, 20), "LONDON WEATHER", fill = (0,255, 0))

#
# Now we enter the city and country details
#
  cty = manager.weather_at_place('London,GB')
  MyWeather = cty.weather

  h =      "Humidity (%) = " + str(MyWeather.humidity)
  temp = MyWeather.temperature('celsius')
  wind = MyWeather.wind()
  p = MyWeather.barometric_pressure()

  tmin =   "Temp Min (C) = " + str(temp['temp_min'])
  tmax =   "Temp Max (C) = " + str(temp['temp_max'])

  wspeed = "Wind (m/s)   = " + str(wind['speed'])
  wdir =   "Wind (deg)   = " + str(wind['deg'])

  press =  "Pressure     = " + str(p['press'])

  draw.text((20, 40), h, fill = (255, 255, 255))
  draw.text((20, 50), tmin, fill = (255, 255, 255))
  draw.text((20, 60), tmax, fill = (255, 255, 255))
  draw.text((20, 70), wspeed, fill = (255, 255, 255))
  draw.text((20, 80), wdir, fill = (255, 255, 255)) 
  draw.text((20, 90), press, fill = (255, 255, 255))
  d = datetime.now().strftime("%d-%m-%y %H:%M:%S")
  draw.text((20, 105), str(d), fill = (0, 255, 0))
  disp.display(img)
  time.sleep(5)

