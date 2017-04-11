# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/10 :18:52$'

import wiringpi as pi
import time
import gpio_setting as PIN

LED = 21
SW = 26
pi.wiringPiSetupGpio()
LED_SET = PIN.Gpioset(LED, 1)
SW_SET = PIN.Gpioset(SW, 2)


while True:
    if PIN.push_sw_1(SW):
        LED = PIN.Led(LED, 1, 0.5)
        LED.flash()
    else:
        LED = PIN.Led(LED, 0)
        LED.flash()