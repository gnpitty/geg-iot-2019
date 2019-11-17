#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
canal = 16 
GPIO.setup(canal, GPIO.OUT)

# On
conta = 18 
pausa = .066666
while conta > 0:
   print(conta)
   GPIO.output(canal, GPIO.LOW)
   sleep(pausa)
   GPIO.output(canal, GPIO.HIGH)
   sleep(pausa)
   conta = conta -1
