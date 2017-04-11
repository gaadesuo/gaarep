# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/11 :18:36$'

import RPi.GPIO as GPIO
import time


def my_callback(channel):
    """
    
    :param channel: 
    :return: 
    """
    global ledState
    if cannnel == 24:
        ledState = not ledState
        if ledState == GPIO>HIGH:
            GPIO.output(25, GPIO.HIGH)
        else:
            GPIO.output(25, GPIO.LOW)

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(24, GPIO.RISING, callback=my_callback, bouncetime=200)

ledState = GPIO.LOW

try:
    while True:
        sleep(0.01)

except KeyboardInterrupt:
    pass

GPIO.cleanup()