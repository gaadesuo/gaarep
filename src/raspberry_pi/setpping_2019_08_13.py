#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2019/08/13 18:22'

import RPi.GPIO as GPIO
import time

"""
GPIOの初期セットアップ
"""
# 変数
coil_a_0 = 12
coil_a_1 = 16
coil_b_0 = 20
coil_b_1 = 21

# GPIOナンバーで書けるように設定
GPIO.setmode(GPIO.BCM)
# モータードライバーへの出力
GPIO.setup(coil_a_0, GPIO.OUT)
GPIO.setup(coil_a_1, GPIO.OUT)
GPIO.setup(coil_b_0, GPIO.OUT)
GPIO.setup(coil_b_1, GPIO.OUT)
# ON_OFFスイッチ
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# センサー
GPIO.setup(25, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)

servo_out = [ 0b1000,
              0b1100,
              0b0100,
              0b0110,
              0b0010,
              0b0011,
              0b0001,
              0b1001]


rotation = [[0, 8 , 1], [6, -1, -1]]
# [0]回転方向,[1]動く前のスリープ、[2]動かした後のスリープ
dance = [[rotation[0], 0.1, 1],
         [rotation[0], 0.1, 1],
         [rotation[0], 0.1, 0.1],
         [rotation[1], 0.01, 0.1],
         [rotation[1], 0.01, 0.1],
         [rotation[1], 0.01, 1],
         [rotation[1], 0.01, 0.01],
         [rotation[1], 0.01, 0.01],
         [rotation[1], 0.01, 0.01],
         [rotation[1], 0.01, 0.01],
         [rotation[1], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[1], 0.01, 0.01],
         [rotation[1], 0.01, 0.01],
         [rotation[1], 0.01, 0.01],
         [rotation[1], 0.01, 0.01],
         [rotation[1], 0.01, 0.01],
         [rotation[1], 0.01, 0.01],
         [rotation[1], 0.01, 0.01],
         [rotation[1], 0.01, 0.01],
         [rotation[1], 0.01, 0.01],
         [rotation[1], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 1],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01],
         [rotation[0], 0.01, 0.01]
         ]

def main():
    try:
        while True:
            time.sleep(0.1)
            # 開始ボタンが押されたか
            if GPIO.input(23) == GPIO.HIGH:
                print("{}".format("開始"))
                for l, t, s in dance:
                    for i in range(l[0], l[1], l[2]):
                        time.sleep(t)
                        GPIO.output(coil_a_0, servo_out[i] & 0b1000)
                        GPIO.output(coil_a_1, servo_out[i] & 0b0010)
                        GPIO.output(coil_b_0, servo_out[i] & 0b0100)
                        GPIO.output(coil_b_1, servo_out[i] & 0b0001)
                    time.sleep(s)

            elif GPIO.input(24) == GPIO.HIGH:
                break

    except KeyboardInterrupt:
        pass
    GPIO.cleanup()


if __name__ == '__main__':
    main()