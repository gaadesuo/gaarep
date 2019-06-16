#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2019/06/15 13:26'

import RPi.GPIO as GPIO

# GPIOセットアップ
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.OUT)


def led_flash(gpio_24):
    """
    GPIO25番を出力する
    """
    GPIO. output(25, GPIO.HIGH) if gpio_24 else GPIO.output(25, GPIO.LOW)


def push_sw_input():
    """
    GPIO24番入力が1ならTrue,0ならFalseを返す(LED制御)
    GPIO12番入力が1ならGPIOを初期化して終了
    """
    while GPIO.input(12) == GPIO.LOW:
        led_flash(True) if GPIO.input(24) == GPIO.HIGH else led_flash(False)

    else:
        print("終了")
        GPIO.cleanup()


def main():
    push_sw_input()


if __name__ == '__main__':
    main()