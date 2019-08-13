#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2019/08/04 05:42'

import RPi.GPIO as GPIO
import time
import sys

"""
GPIOの初期セットアップ
"""
# GPIOナンバーで書けるように設定
GPIO.setmode(GPIO.BCM)
# モーター正転
GPIO.setup(20, GPIO.OUT)
# モーター逆転
GPIO.setup(21, GPIO.OUT)

# スイッチ(プルダウン設定)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# PWM設定(GPIO_NO, 周波数)
normal_rotation = GPIO.PWM(20, 100)
reverse = GPIO.PWM(21, 100)

# デューティー比の初期化
normal_rotation.start(0)
reverse.start(0)

# 変数
normal_num = 0
revers_num = 0


def start_sw():
    """
    スタートスイッチが押されたときTrueを返す
    return: bool
    """
    if GPIO.input(12) == GPIO.HIGH:
        return True

def motor_pwm():
    """
    モーターの回転を制御
    """
    global normal_num
    global revers_num

    while True:
        time.sleep(0.1)
        print(normal_num, revers_num)
        # ボタン入力でduty比の変更
        if GPIO.input(6) == GPIO.HIGH and normal_num < 100:
            # print("GPIO_6_ON")
            normal_num += 10
        elif GPIO.input(13) == GPIO.HIGH and normal_num > 0:
            # print("GPIO_13_ON")
            normal_num -= 10
        elif GPIO.input(19) == GPIO.HIGH and revers_num < 100:
            # print("GPIO_19_ON")
            revers_num += 10
        elif GPIO.input(26) == GPIO.HIGH and revers_num > 0:
            # print("GPIO_26_ON")
            revers_num -= 10

        # 回転制御。正転逆転どちらも1以上ならブレーキ
        if (normal_num > 0 and revers_num > 0):
            # print(normal_num, revers_num)
            # print("ブレーキ")
            normal_rotation.ChangeDutyCycle(100)
            reverse.ChangeDutyCycle(100)
            time.sleep(0.1)
            normal_num = 0
            revers_num = 0
        elif normal_num > 0 and revers_num == 0:
            normal_rotation.ChangeDutyCycle(normal_num)
            reverse.ChangeDutyCycle(0)
        elif revers_num > 0 and normal_num == 0:
            reverse.ChangeDutyCycle(revers_num)
            normal_rotation.ChangeDutyCycle(0)

        if GPIO.input(16) == GPIO.HIGH:
            normal_rotation.ChangeDutyCycle(0)
            reverse.ChangeDutyCycle(0)
            break

def main():
    try:
        while True:
            if start_sw():
                print("toggle_on")
                time.sleep(1)
                motor_pwm()
            elif GPIO.input(16) == GPIO.HIGH:
                break

    except KeyboardInterrupt:
        GPIO.cleanup()
    GPIO.cleanup()

if __name__ == '__main__':
    main()