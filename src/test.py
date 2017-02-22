#! /usr/bin/python#
# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "user"
__date__ = "$2017/02/21 18:21:41$"


import wiringpi as GPIO
import time

#-----GPIOの設定-----


LED = 26      #左側NO19

GPIO.wiringPiSetupGpio()
GPIO.pinMode(LED,GPIO.OUTPUT)


#-----関数定義-----


def output(device,style):
    """GPIOの出力"""
    GPIO.digitalWrite(device,style)


#-----LEDを光らせる-----


for lp1 in range(2):
    output(LED,GPIO.HIGH)
    time.sleep(1)
    output(led,GPIO.LOW)
    time.sleep(1)
 