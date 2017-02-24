#! /usr/bin/python
# :-*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "user"
__date__ = "$2017/02/24 19:10:13$"


import wiringpi as GPIO
from time import sleep

buzzer = 26        #左19

GPIO.wiringPiSetupGpio()
GPIO.softToneCreate(buzzer)

do = 262

if __name__ == "__main__":
    for lp1 in range(3):
        GPIO.softToneWrite(buzzer,do)
        sleep(1)
        GPIO.softToneWrite(buzzer,0)
        sleep(0.5)

