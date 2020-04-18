#!/usr/bin/python
from gpiozero import RGBLED, Button
from time import sleep
import random

led = RGBLED(red=20,green=19,blue=18)

while True:
	led.value=(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
	sleep(0.3)