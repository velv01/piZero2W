/*================================================
      ARDUINO UNO - RASPBERRY PI ZERO 2 W COMMS
      =========================================
In this project a button is connectd to Arduino Uno
pin 2. HC-06 Bluetooth module is connected to pin 3
The program sends command "1" over the Bluetooth when
the button is pressed

Autjor: Dogan Ibrahim
File  : ardprog
Date  : December, 2022
==================================================*/
#include <SoftwareSerial.h>
SoftwareSerial MySerial(4, 3);        // rx, tx

int Button = 2;                       // Button at pin 2

void setup() 
{
  MySerial.begin(9600);               // Baud rate
  pinMode(Button, INPUT);             // Button is input
}

//
// MAin program looop
//
void loop() 
{
  while (digitalRead(Button) == 1);   // Button not pressed
  while (digitalRead(Button) == 0);   // Button not released
  MySerial.print("1");                // Send "1"
  delay(1000);
}
