#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2019/06/16 14:12'

import RPiGPIO as GPIO
import time
import threading


"""
ver 0.01

仕様と変更点

2019/06/16 ver0.01

アナログからデジタルに変更の為初期仕様から変更をする
プレス、排出のリミットスイッチをデジタル化にする
それに伴い各LSスイッチの排除
手動自動共に内部変数によるカウントで制御
MAXを100とし初期位置は0とする
100の時は各々のLEDを常時点灯、1～99の時は0.5秒の点滅とする
"""

"""
今後の予定

LS廃止の為GPIOに空きができたので終了スイッチの増設
それに伴いキーボードでの強制終了の廃止
排出シリンダーLEDの制御でマニュアル側は完成の予定
LED制御はauto側を書くときはコードの追加
"""


"""
GPIOセットアップ
"""


# GPIOナンバーでコードを書けるように設定
GPIO.setmode(GPIO.BCM)
# 手動モードSW
GPIO.setup(4, GPIO.IN)
# 自動モードSW
GPIO.setup(17, GPIO.IN)
# 手動プレスSW
GPIO.setup(27, GPIO.IN)
# 手動排出SW
GPIO.setup(22, GPIO.IN)
# 自動ON
GPIO.setup(5, GPIO.IN)
# 自動OFF
GPIO.setup(6, GPIO.IN)
# プレス戻りLS
GPIO.setup(13, GPIO.IN)
# プレス出LS
GPIO.setup(19, GPIO.IN)
# 排出戻りLS
GPIO.setup(26, GPIO.IN)
# 排出出LS
GPIO.setup(23, GPIO.IN)
# 検出LS
GPIO.setup(24, GPIO.IN)
# 手動モードLED
GPIO.setup(25, GPIO.OUT)
# 自動モードLED
GPIO.setup(12, GPIO.OUT)
# 自動ONLED
GPIO.setup(16, GPIO.OUT)
# プレスSV起動中LED
GPIO.setup(20, GPIO.OUT)
# 排出SV起動中LED
GPIO.setup(21, GPIO.OUT)


"""
関数定義
"""


def mode_selection():
    """
    モード変更
    手動モード(GPIO_4)が入力されたときにmode_numに1を代入
    自動モード(GPIO_17)が入力されたときにmode_numに2を代入
    """
    while True:
        global mode_num
        while True:
            if GPIO.input(4) == GPIO.HIGH:
                mode_num = 1
            elif GPIO.input(17) == GPIO.HIGH:
                mode_num = 2


def man_press_sl_count():
    """
    マニュアル時プレスシリンダーのカウントを制御
    カウントアップの条件
     1 マニュアル時
     2 手動プレス(GPIO_17)が押されている
     3 手動排出ボタンが押されていない
     4 排出シリンダーが初期位置
     5 プレスカウンターがMAXではない
    それ以外の時はカウントを減らす
    0 <= pres_sl_counter <= 100
    """
    global press_sl_counter
    while True:
        while mode_num == 1 & GPIO.input(27) == GPIO.HIGH \
                & GPIO.input(22) == GPIO.LOW & outer_sl_counter == 0 \
                & press_sl_counter < 100:
            press_sl_counter += 1
        else:
            if press_sl_counter > 0:
                press_sl_counter -= 1


def man_outer_sl_count():
    """
    マニュアル時排出シリンダーのカウントを制御
    カウントアップの条件
     1 マニュアル時
     2 手動排出が押されている
     3 手動プレスが押されていない
     4 プレスシリンダーが初期位置
     5 排出カウンターがMAXではない
    0 <= outer_sl_counter <= 100
    """
    global outer_sl_counter
    while True:
        while mode_num == 1 & GPIO.input(22) == GPIO.HIGH \
                & GPIO.input(27) == GPIO.LOW & press_sl_counter == 0 \
                & outer_sl_counter < 100:
            outer_sl_counter += 1
        else:
            if outer_sl_counter > 0:
                outer_sl_counter -= 1


def press_sl_led_flash():
    """
    プレスシリンダーLED(GPIO_20)の制御
    """
    while True:
        if press_sl_counter == 0:
            GPIO.output(20, GPIO.LOW)
        while 100 > press_sl_counter > 0:
            GPIO.output(20, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(20, GPIO.LOW)
            time.sleep(0.5)
        while press_sl_counter == 100:
            GPIO.output(20, GPIO.HIGH)


"""
main関数
"""


def main():
    try:
        mode_selection.start()
        man_press_sl_count.start()
        man_outer_sl_count.start()
        press_sl_led_flash.start()

    except KeyboardInterrupt:
        GPIO.cleanup()


"""
グローバル変数定義
"""


mode_num = 0
press_sl_counter = 0
outer_sl_counter = 0


"""
マルチスレッド準備
"""


mode_selection = threading.Thread(target=mode_selection)
man_press_sl_count = threading.Thread(target=man_press_sl_count)
man_outer_sl_count = threading.Thread(target=man_outer_sl_count)
press_sl_led_flash = threading.Thread(target=press_sl_led_flash)


"""
開始
"""


if __name__ == '__main__':
    main()
