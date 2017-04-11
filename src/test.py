# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/10 :18:52$'

import wiringpi as pi
import time
import gpio_setting as PIN

pi.wiringPiSetupGpio()
GPIO.pinMode(21, GPIO.OUTPUT)

while True:
    if PIN.push_sw_1(26):
        LED = PIN.Led(21, 1, 0.5)
        LED.flash()
    else:
        LED = PIN.Led(21, 0)
        LED.flash()