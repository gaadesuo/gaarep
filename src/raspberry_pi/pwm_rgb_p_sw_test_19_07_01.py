#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2019/06/30 11:33'

import RPi.GPIO as GPIO
import threading
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
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.IN)
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


def r_sw():
    """
    赤色スイッチ(GPIO13)を押されたときTrueを返す
    押されていない時はFalseを返す
    :return: bool型
    """
    if GPIO.input(13) == GPIO.HIGH:
        return True
    else:
        return False


def g_sw():
    """
    緑色スイッチ(GPIO19)を押されたときTrueを返す
    押されていない時はFalseを返す
    :return: bool型
    """
    if GPIO.input(19) == GPIO.HIGH:
        return True
    else:
        return False


def b_sw():
    """
    青色スイッチ(GPIO26)を押されたときTrueを返す
    押されていない時はFalseを返す
    :return: bool型
    """
    if GPIO.input(26) == GPIO.HIGH:
        return True
    else:
        return False


def count_down():
    """
    一秒ごとに1を返す
    :return: 1 (int)
    """
    time.sleep(0.1)
    return 1


def led_flash():
    """
    フルカラーLEDのデューティー比を操作する
    """
    # カウント初期値
    r_count = 0
    g_count = 0
    b_count = 0

    # 並列処理準備
    thread_r = threading.Thread(target=r_sw)
    thread_g = threading.Thread(target=g_sw)
    thread_b = threading.Thread(target=b_sw)
    thread_countdown = threading.Thread(target=count_down)
    thread_r.start()
    thread_g.start()
    thread_b.start()
    thread_countdown.start()

    while True:
        # print("{}{}{}".format(r_count, g_count, b_count))
        if stop_sw():
            break

        # アノードコモンの為100からデューティー比の値を引く
        r.ChangeDutyCycle(100 - r_count)
        g.ChangeDutyCycle(100 - g_count)
        b.ChangeDutyCycle(100 - b_count)

        # RGBボタンが押されて各々のデューティ比が100より低い時
        # 各デューティー比を1上げる。100の場合はそのままループ
        if r_count == 100:
            pass
        elif r_sw() == 1 and r_count < 100:
            time.sleep(0.1)
            print("r_{}".format(r_count))
            r_count += 1
        if g_count == 100:
            pass
        elif g_sw() == 1 and g_count < 100:
            time.sleep(0.1)
            print("g_{}".format(g_count))
            g_count += 1
        if b_count == 100:
            pass
        elif b_sw() == 1 and b_count < 100:
            time.sleep(0.1)
            print("b_{}".format(b_count))
            b_count += 1

        # RGBボタンが押されていなくて各々のデューティー比が
        # 0より大きい時は0.1秒ごとにデューティー比を1下げる
        if r_sw() == 0 and r_count > 0:
            print(r_count)
            r_count -= count_down()
        elif g_sw() == 0 and g_count > 0:
            print(g_count)
            g_count -= count_down()
        elif b_sw() == 0 and b_count > 0:
            print(b_count)
            b_count -= count_down()


def start_sw():
    """
    スタートスイッチ(GPIO_5)が入力されるとTrueを返す
    :return: True
    """
    if GPIO.input(5) == GPIO.HIGH:
        return True


def stop_sw():
    """
    ストップスイッチ(GPIO_6)が入力されるとTrueを返す
    :return: True
    """
    if GPIO.input(6) == GPIO.HIGH:
        return True


def main():
    try:
        while True:
            if start_sw():
                led_flash()
            elif stop_sw():
                break

        # GPIO初期化
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
