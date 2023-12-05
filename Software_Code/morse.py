#-----------------------------------------------------------------
#
#                  MORSE CODE EXERCISER
#                  ====================
#
# This project can be used to learn the Morse code. A buzzer is
# connected to GPIO 2 of the Zero 2 W.
#
# The program reads a text from the keyboard and then sounds the
# buzzer to simulate sending or receiving the Morse code of this
# text.
#
# In this project the Morse code speed is assumed to be 10 wpm,
# but can easily be changed by changing the parameter wpm.
#
# File  : morse.py
# Date  : December, 2022
# Author: Dogan Ibrahim
#-----------------------------------------------------------------
import RPi.GPIO as GPIO			# import GPIO module
import time				# import time module
GPIO.setwarnings(False)

Pin = 2
words_per_minute = 10			# define words per min
wpm = 1200/words_per_minute		# unit time in milliseconds
unit_time = wpm / 1000

GPIO.setmode(GPIO.BCM)			# set BCM pin numbering
GPIO.setup(Pin, GPIO.OUT)		# Configure GPIO 2 as output

Morse_Code = {
         'A': '.-',
         'B': '-...',
         'C': '-.-.',
         'D': '-..',
         'E': '.',
         'F': '..-.',
         'G': '--.',
         'H': '....',
         'I': '..',
         'J': '.---',
         'K': '-.-',
         'L': '.-..',
         'M': '--',
         'N': '-.',
         'O': '---',
         'P': '.--.',
         'Q': '--.-',
         'R': '.-.',
         'S': '...',
         'T': '-',
         'U': '..-',
         'V': '...-',
         'W': '.--',
         'X': '-..-',
         'Y': '-.--',
         'Z': '--..'
         }

#
# This function sends a DOT (unit time)
#
def DO_DOT():
   GPIO.output(Pin, 1)
   time.sleep(unit_time)
   GPIO.output(Pin, 0)
   time.sleep(unit_time)
   return

#
# This function sends a DASH ( 3*unit time)
#
def DO_DASH():
   GPIO.output(Pin, 1)
   time.sleep(3*unit_time)
   GPIO.output(Pin, 0)
   time.sleep(unit_time)
   return

#
# This function sends inter-word space (7*unit time)
#
def DO_SPACE():
   time.sleep(7*unit_time)
   return

#
# Main program code
#
text = ""
while text != "QUIT":
   text = input("Enter text to send: ")
   if text != "QUIT":
      for letter in text:
         if letter == ' ':
            DO_SPACE()
         else:
            for code in Morse_Code[letter.upper()]:
               if code == '-':
                  DO_DASH()
               elif code == '.':
                  DO_DOT()
               time.sleep(unit_time)
   time.sleep(2)


