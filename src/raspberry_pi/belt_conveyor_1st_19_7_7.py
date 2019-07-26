#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2019/07/07 13:06'


import RPi.GPIO as GPIO
import time
import threading


"""
仕様
2019/07/07
ベルトコンベアとSVはduty比で流れを表現
duty比100でリミットスイッチ到達

"""


"""
GPIOのセットアップ
"""
# GPIOナンバーでコードを掛けるように設定
GPIO.setmode(GPIO.BCM)

# LED青
GPIO.setup(22, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
# LED赤
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
# LED黄
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
# LED緑
GPIO.setup(21, GPIO.OUT)

# スイッチ
GPIO.setup(18, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

# PWM設定
start_ls = GPIO.PWM(22, 50)
turn_table_ls = GPIO.PWM(6, 50)
outer_ls = GPIO.PWM(5, 50)
belcon_in_led = GPIO.PWM(13, 50)
belcon_out_led = GPIO.PWM(19, 50)
turn_table_n_rotation = GPIO.PWM(26, 50)
turn_table_reverse = GPIO.PWM(12, 50)
turn_table_start = GPIO.PWM(16, 50)
turn_table_outer = GPIO.PWM(20, 50)
turn_table_SV = GPIO.PWM(21, 50)

# 初期Duty比の値
# 100で消灯 0で点灯
start_ls.start(100)
turn_table_ls.start(100)
outer_ls.start(100)
belcon_in_led.start(100)
belcon_out_led.start(100)
turn_table_n_rotation.start(100)
turn_table_reverse.start(100)
turn_table_start.start(100)
turn_table_outer.start(100)
turn_table_SV.start(100)


"""
スイッチ入力関数
"""


def start_sw():
    """
    スタートスイッチ(GPIO18)が入力されるとTrueを返す
    :return: True
    """
    if GPIO.input(18) == GPIO.HIGH:
        return True


def stop_sw():
    """
    ストップスイッチ(GPIO23)が入力されるとTrueを返す
    :return: True
    """
    if GPIO.input(23) == GPIO.HIGH:
        return True


def work_entry():
    """
    ワーク投入スイッチ(GPIO24)が入力されたときにTrueを返す
    :return: True
    """
    if GPIO.input(24) == GPIO.HIGH:
        return True


def work_discharge():
    """
    ワーク取り除きスイッチ(GPIO25)が入力されたときにTrueを返す
    :return: True
    """
    if GPIO.input(25) == GPIO.HIGH:
        return True


"""
LED制御関数
"""


def start_ls_led(flag):
    """
    ワーク検知LSのLEDを制御。
    :param flag:Trueなら点灯、Falseなら消灯
    """
    if flag:
        start_ls.ChangeDutyCycle(0)
        time.sleep(0.5)
    else:
        start_ls.ChangeDutyCycle(100)


def outer_ls_led(flag):
    """
    ワーク排出検出のLEDを制御
    :param flag: Trueなら点灯、Falseなら消灯
    :return: 点灯時は True 消灯時はFalseを返す
    """
    if flag:
        outer_ls.ChangeDutyCycle(0)
        time.sleep(0.5)
        return True
    else:
        outer_ls.ChangeDutyCycle(100)
        return False


def turn_t_ls_led(flag):
    """
    ターンテーブル到着LEDを点滅させる
    :param flag: Trueなら点灯Falseなら消灯
    :return: 点灯時は True 消灯時はFalseを返す
    """
    if flag:
        turn_table_ls.ChangeDutyCycle(0)
        time.sleep(0.5)
        return True
    else:
        turn_table_ls.ChangeDutyCycle(100)
        return False


def red_led(flag):
    """
    1なら搬入側、2なら排出側のベルコンが動く
    0の時は消灯
    :param flag: 0 消灯 1 入り口側点灯 2 出口側点灯
    """
    duty = 0
    if flag == 1:
        while duty < 100:
            duty += 2
            # print("搬入コンベアLED数値【{}】".format(duty))
            belcon_in_led.ChangeDutyCycle(100 - duty)
            turn_table_n_rotation.ChangeDutyCycle(100 - duty)
            time.sleep(0.1)

    elif flag == 2:
        while duty < 100:
            duty += 2
            belcon_out_led.ChangeDutyCycle(100 - duty)
            turn_table_reverse.ChangeDutyCycle(100 - duty)
            time.sleep(0.1)

    elif flag == 0:
        # print("搬入コンベアLED数値【0】")
        belcon_in_led.ChangeDutyCycle(100)
        turn_table_n_rotation.ChangeDutyCycle(100)
        belcon_out_led.ChangeDutyCycle(100)
        turn_table_reverse.ChangeDutyCycle(100)


def yellow_led(sv_duty):
    """
    黄色LEDを制御する
    :param sv_duty: SVの位置
    """
    if sv_duty == 0:
        turn_table_start.ChangeDutyCycle(0)
        turn_table_outer.ChangeDutyCycle(100)
    elif sv_duty == 100:
        turn_table_start.ChangeDutyCycle(100)
        turn_table_outer.ChangeDutyCycle(0)
    else:
        turn_table_start.ChangeDutyCycle(100)
        turn_table_outer.ChangeDutyCycle(100)


def green_led(flag):
    """
    SVスイッチLEDを制御
    :param flag: True ならSVON FalseならOFF
    """
    if flag:
        duty = 0
        while duty < 100:
            # print("SVLEDの数値【{}】".format(duty))
            duty += 5
            turn_table_SV.ChangeDutyCycle(100 - duty)
            time.sleep(0.1)
    else:
        duty = 100
        while duty > 0:
            duty -= 5
            turn_table_SV.ChangeDutyCycle(100 - duty)
            time.sleep(0.1)


"""
制御部
"""


def in_control(l_t_t_ls_flag):
    """
    ワーク入り口からターンテーブル到着までの制御
    :param l_yellow_duty: ターンテーブルの位置
    :param l_t_t_ls_flag: ターンテーブル上に荷物があってたまってないか
    :return: bool ターンテーブル到着のフラグ True
    """
    start_ls_led(True)
    while l_t_t_ls_flag != 0:
        if work_discharge():
            return True
        continue
    start_ls_led(False)
    red_led(1)
    red_led(0)
    return turn_t_ls_led(True)


def out_control(l_out_ls_led_flag):
    """
    ターンテーブルから排出し排出LS検知まで到着の制御
    :param l_out_ls_led_flag: 排出LSのフラグ
    :return: bool 排出LSの値 True
    """
    if l_out_ls_led_flag == 0:
        red_led(2)
        red_led(0)
        return outer_ls_led(True)


def turn_table_control(flag):
    """
    ターンテーブルの制御
    :param flag: TrueならSVON FalseならSVOFF
    :return: bool svがONならTrue、OFFならFalseを返す
    """
    if flag:
        turn_t_ls_led(False)
        yellow_led(1)
        green_led(True)
        yellow_led(100)
        return True
    else:
        yellow_led(1)
        green_led(False)
        yellow_led(0)
        return False


def main_control():
    """
    全体の制御部
    """
    # 変数初期化
    outer_ls_flag = 0
    t_t_ls_flag = 0
    third_flag = 0

    while True:
        yellow_led(0)
        # 一個目のワークを投入
        if work_entry():
            t_t_ls_flag = in_control(t_t_ls_flag)
            if outer_ls_flag == 0:
                turn_table_control(True)
                outer_ls_flag = out_control(outer_ls_flag)
                t_t_ls_flag = turn_table_control(False)
            while True:
                # ワークが排出、投入待ちへ
                if work_discharge():
                    outer_ls_flag = outer_ls_led(False)
                    break
                # 二個目のワークを投入
                elif work_entry():
                    t_t_ls_flag = in_control(t_t_ls_flag)
                    while True:
                        # 一個目のワークが排出、移動処理
                        if work_discharge():
                            outer_ls_flag = outer_ls_led(False)
                            turn_table_control(True)
                            outer_ls_flag = out_control(outer_ls_flag)
                            t_t_ls_flag = turn_table_control(False)
                            # 三個目のワークがある場合の移動処理
                            if third_flag == 1:
                                t_t_ls_flag = in_control(0)
                                third_flag = 0
                                continue
                            break
                        # 三個目のワークを投入
                        elif work_entry():
                            third_flag = in_control(t_t_ls_flag)

                        elif stop_sw():
                            break

                elif stop_sw():
                    break

        if stop_sw():
            break


"""
デバッグ用
"""


def debug():
    """
    初期デバッグ用
    """
    while True:
        if work_entry():
            print("ワーク置いたよ")
            time.sleep(0.1)
        if work_discharge():
            print("ワーク取ったよ")
            time.sleep(0.1)
        start_ls.ChangeDutyCycle(0)
        turn_table_ls.ChangeDutyCycle(0)
        outer_ls.ChangeDutyCycle(0)
        belcon_in_led.ChangeDutyCycle(0)
        belcon_out_led.ChangeDutyCycle(0)
        turn_table_n_rotation.ChangeDutyCycle(0)
        turn_table_reverse.ChangeDutyCycle(0)
        turn_table_SV.ChangeDutyCycle(0)
        turn_table_start.ChangeDutyCycle(0)
        turn_table_outer.ChangeDutyCycle(0)
        if stop_sw() == 1:
            break


def main():
    try:
        while True:
            if start_sw():
                print("スタート")
                # debug()
                main_control()
            elif stop_sw():
                print("終了")
                GPIO.cleanup()
                break
    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == '__main__':
    main()