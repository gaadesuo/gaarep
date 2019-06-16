#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2019/06/15 10:18'


import RPi.GPIO as GPIO
import time

# GPIOセットアップ
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)


def led_flash():
    """
    LEDを1秒間隔で10回点滅させる
    """
    for i in range(10):
        GPIO.output(25, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(25, GPIO.LOW)
        time.sleep(0.5)


def main():
    led_flash()

    GPIO.cleanup()


if __name__ == '__main__':
    main()