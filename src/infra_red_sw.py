# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/23 :22:44$'

import gpio_setting as GPIO
import wiringpi as PIN
import time


def main():
    pass


if __name__ == '__main__':
    main()

    # GPIO 初期設定
    PIN.wiringPiSetupGpio()
    PIN.pinMode(5, PIN.INPUT)
    PIN.pinMode(21, PIN.OUTPUT)

    while True:
        if GPIO.slide_sw_1(5):
            print("ok")
            LED = GPIO.Led(21, 1)
            LED.flash()
            time.sleep(0.1)
        else:
            LED = GPIO.Led(21, 2)
            LED.flash()
            print("NG")
            time.sleep(0.1)
