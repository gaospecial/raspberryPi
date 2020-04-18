#!/usr/bin/python
from gpiozero import RGBLED, Button
from time import sleep
import random

led = RGBLED(red=20,green=19,blue=18)
touch = Button(12)

def light():
	led.value=(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))

def loop():
	while True:
		if touch.is_pressed:
			light()


def destroy():
	led.value=(0,0,0)


try:
	loop()
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
	destroy()
