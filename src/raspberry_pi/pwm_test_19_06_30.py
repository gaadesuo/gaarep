#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2019/06/30 11:33'

import RPi.GPIO as GPIO
import time


"""
GPIOのセットアップ
"""
# GPIOナンバーでコードを書けるように設定
GPIO.setmode(GPIO.BCM)
# LED
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

# スイッチ
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)

# PWM設定(GPIO_NO, 周波数(50Hz))
r = GPIO.PWM(16, 50)
g = GPIO.PWM(20, 50)
b = GPIO.PWM(21, 50)

# 初期デューティー比の初期値
# アノードコモンの為100で消灯 0で全灯
r.start(100)
g.start(100)
b.start(100)


def led_flash():
    """
    フルカラーLEDを光らせる
    赤 デューティー比を5カウントづつ上げ100で初期化
    緑 デューティー比を10カウントづつ上げ100で初期化
    青 デューティー比を20カウントづつ上げ100で初期化

    :param r_duty: 赤のデューティー変数
    :param g_duty: 緑のデューティー変数
    :param b_duty: 青のデューティー変数
    """
    # カウント初期値
    r_count = 0
    g_count = 0
    b_count = 0
    while True:
        # アノードコモンの為100からデューティー比の値を引く
        r.ChangeDutyCycle(100 - r_count)
        g.ChangeDutyCycle(100 - g_count)
        b.ChangeDutyCycle(100 - b_count)
        r_count += 5
        g_count += 10
        b_count += 20
        if r_count == 100:
            r_count = 0
        if g_count == 100:
            g_count = 0
        if b_count == 100:
            b_count = 0
        time.sleep(0.5)
        if stop_sw():
            break


def start_sw():
    """
    スタートスイッチ(GPIO_19)が入力されるとled_flash関数を呼ぶ
    """
    if GPIO.input(19) == GPIO.HIGH:
        led_flash()


def stop_sw():
    """
    ストップスイッチ(GPIO_26)が入力されるとTrueを返す
    :return: True
    """
    if GPIO.input(26) == GPIO.HIGH:
        return True


def main():
    while True:
        start_sw()
        if stop_sw():
            break

    # GPIO初期化
    GPIO.cleanup()


if __name__ == '__main__':
    main()
