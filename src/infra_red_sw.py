# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/23 :22:44$'

import gpio_setting as GPIO
import RPi.GPIO as PIN
import time


def main():
    pass


if __name__ == '__main__':
    main()

    while True:
        if GPIO.push_sw_1(5):
            print("ok")
            LED = GPIO.Led(21, 1)
            LED.flash()
            LED = GPIO.Led(21, 2)
            LED.flash()
        else:
            print("NG")
            time.sleep(0.1)
