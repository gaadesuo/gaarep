#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2019/06/30 11:33'

import RPi.GPIO as GPIO
import threading


"""
GPIOのセットアップ
"""
# LED
GPIO.setup(16, GPIO.IN)
GPIO.setup(20, GPIO.IN)
GPIO.setup(21, GPIO.IN)

# スイッチ
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)

# PWM設定(GPIO_NO, 周波数(50Hz))
r = GPIO.PWM(16, 50)
g = GPIO.PWM(20, 50)
b = GPIO.PWM(21, 50)

# 初期デューティー比の値(0)
r.start(0)
g.start(0)
b.start(0)


def start_sw():
    """
    スタートスイッチ(GPIO_19)が入力されるとTrueを返す
    :return: True
    """
    while True:
        if GPIO.input(19) == GPIO.HIGH:
            return True


def stop_sw():
    """
    ストップスイッチ(GPIO_26)が入力されるとTrueを返す
    :return: True
    """
    while True:
        if GPIO.input(26) == GPIO.HIGH:
            return True


def main():
    # 並行処理
    thread_start_sw = threading.Thread(target=start_sw)
    thread_stop_sw = threading.Thread(target=stop_sw)

    thread_start_sw.start()
    thread_stop_sw.start()
    while True:
        if start_sw():
            print("ok")
        elif stop_sw():
            break

    GPIO.cleanup()


if __name__ == '__main__':
    main()
