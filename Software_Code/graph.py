#-------------------------------------------------------------------
#       REAL TIME GRAPH OF HUMIDITY AND TEMPERATURE
#       ===========================================
#
# This program reads the ambient temperature and himidity from
# a DHT11 type sensor and displays them on the monitor in real-time
# as a graph.
#
# In this program data is collected every 2 seconds, for a period
# of 100 seconds.
#
# Program: graph.py
# Date   : December, 2022
# Author : Dogan Ibrahim
#------------------------------------------------------------------
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
GPIO = 2

#
# Start of main program. Humidity and temperature are read from
# DHT11 and are plotted in real time as the data are being read
#
plt.axis([0,100,0,100])
plt.title('Humidity and Temperature')
plt.xlabel('Time')
plt.ylabel('Hum. & Temp')
plt.clf()

j=1
plt.ion()

for i in range (0,102,2):
    humidity,temperature = Adafruit_DHT.read_retry(sensor,GPIO)
    x = float(i)
    t = float(temperature)
    h = float(humidity)
    plt.scatter(x,t,color='blue',label='Tempeature')
    plt.scatter(x,h,color='black',label='Humidity')
    plt.draw()
    if j == 1:
        j=0
        plt.legend()
    plt.pause(0.0001)
    time.sleep(5)
    




