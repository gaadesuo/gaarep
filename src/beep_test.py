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

delay = 0.2
do = 262
re = 294
mi = 330
fa = 349
so = 392
ra = 440
si = 494
hdo = 523
hre = 587
hmi = 659
non = 0

pnpu = (re,re,do,do,re,so,ra)

if __name__ == "__main__":
    for yodo in onpu:
        GPIO.softToneWrite(buzzer,yodo)
        sleep(delay * 2)
        GPIO.softToneWrite(buzzer,0)
        sleep(delay)

