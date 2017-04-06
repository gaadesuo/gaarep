# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/02 :20:02$'

import time
import wiringpi as GPIO

# GPIOの初期化
GPIO.wiringPiSetupGpio()

"""

CLASS

"""


class Led1:
    """

    :param mode: 
    :param pin: 
    :param timer: 
    :param pwm: 
    """
    def __init__(self, pin, mode, timer=1, pwm=100, count=1):
        self.pin = pin
        self.mode = mode
        self.timer = timer
        self.pwm = pwm
        self.count = count

    def flash(self):
        LED1 = self.pin
        GPIO.pinMode(LED1, GPIO.OUTPUT)
        GPIO.softPwmCreate(LED1, 0, 100)
        if self.mode == 1:
            GPIO.softPwmWrite(LED1, self.pwm)
            time.sleep(self.timer)
        if self.mode == 2:
            for lp1 in range(self.count):
                GPIO.softPwmCreate(LED1, self.pwm)
                time.sleep(self.timer)
                GPIO.digitalWrite(LED1, LOW)
                time.sleep(self.timer)
        if self.mode == 3:
            GPIO.digitalWrite(LED1.LOW)


led1 = Led1(0,0,0,0)
led1.flash()
