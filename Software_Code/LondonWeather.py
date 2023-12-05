#=======================================================
#     DISPLAY LONDON WEATHER IN REAL-TIME
#
# This program fetches the real-time weather data
# for a give city from Open Weather MAp and displays
# on the screen every 15 seconds
#
# Author: Dogan Ibrahim
# File  : LondonWeather.py
# Date  : January, 2023
#=======================================================
from pyowm import OWM		# import Open Weather Map
import time			# import time

#
# Enter your API key below
#
weather = OWM('05ff9a8a5d66e4f3115c5YOUR API')
manager = weather.weather_manager()

#
# Now we enter the city and country details
#
cty = manager.weather_at_place('London,GB')
MyWeather = cty.weather

while True:
   W = MyWeather.wind()
   print("       Wind: ", W['speed'], " m/s")
   print("       Wind: ", W['deg'], " Degrees")

   print("   Humidity: " , MyWeather.humidity)

   print("       Rain: " , MyWeather.rain)

   T =  MyWeather.temperature('celsius')
   print("   Min Temp: ", T['temp_min'], " C")
   print("   Max Temp: ", T['temp_max'], " C")
   print(" Feels like: ", T['feels_like'], " C")

   print("   Pressure: ", MyWeather.barometric_pressure(), " hPa")

   print("     Clouds: " , MyWeather.clouds)

   print("Visibility : ", MyWeather.visibility_distance, " km")

   print("    Sunrise: ", MyWeather.sunrise_time(timeformat='date'))
   print("     Sunset: ", MyWeather.sunset_time(timeformat='date'))

   time.sleep(15)

