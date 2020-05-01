#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Adafruit_DHT as DHT
import time
import pygame

Sensor = 11
# 温湿度传感器的 GPIO 针脚
humiture = 21  

pygame.init()

alert = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Center.wav")


def setup():
    print 'Setting up, please wait...'

def loop():
    while True:
        humidity, temperature = DHT.read_retry(Sensor, humiture)
        localtime = time.asctime( time.localtime(time.time()) )

        if humidity is not None and temperature is not None:
            print '%30s; %2.1f; %2.1f%%' % (localtime, temperature, humidity)
        else:
            print 'Failed to get reading. Try again!'

        if temperature > 37:
            alert.play()
# 一秒钟检测一次
        time.sleep(1)  
# 一分钟检测一次
#        time.sleep(60) 


setup()
try:
    loop()
except KeyboardInterrupt:
    pygame.mixer.stop()
