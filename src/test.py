# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/10 :18:52$'

import wiringpi as pi
import time
import gpio_setting as PIN

LED = 21
SW = 26
pi.wiringPiSetupGpio()
LED_SET = PIN.Gpioset(21, 1)
SW_SET = PIN.Gpioset(26, 2)


while True:
    if PIN.push_sw_1(26):
        LED = PIN.Led(int(LED), 1, 0.5)
        LED.flash()
    else:
        LED = PIN.Led(21, 0)
        LED.flash()