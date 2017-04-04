# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/02 :20:02$'

import time
import wiringpi as GPIO

# GPIOの初期化
GPIO.wiringPiSetupGpio()

"""*****注意*****

関数を呼び出す際にはpin番号の値を与える事。値はint

*****"""


"""

LED関数

"""


def led_flash_1(interval , pin):
    """
        *****注意*****
    関数を呼び出す際にはpin番号の値を与える事。
        ---GPIO出力---
    与えられたpin NOのGPIO PINのLEDを関数に与えられた値/10秒間点滅させる
    :param interval: int: 点滅間隔の設定。与えられたの/10感覚で点滅させる
    :param pin: int: LEDのGPIO PIN NO
    """
    LED1 = pin
    GPIO.pinMode(LED1, GPIO.OUTPUT)
    GPIO.digitalWrite(LED1, GPIO.HIGH)
    time.sleep(interval / 10)
    GPIO.digitalWrite(LED1, GPIO.LOW)
    time.sleep(interval / 10)


def led_flash_2(intterval, pin):
    """
        *****注意*****
    関数を呼び出す際にはpin番号の値を与える事。
    値を忘れるとエラーなのでtry文を忘れない。
        ---GPIO出力---
    与えられたpin NOのGPIO PINのLEDを関数に与えられた値/10秒間点滅させる
    :param interval: int: 点滅間隔の設定。与えられたの/10感覚で点滅させる
    :param pin: int: LEDのGPIO PIN NO
    """
    LED2 = pin
    GPIO.pinMode(LED2, GPIO.OUTPUT)
    GPIO.digitalWrite(LED2, GPIO.HIGH)
    time.sleep(intterval / 10)
    GPIO.digitalWrite(LED2, GPIO.LOW)
    time.sleep((intterval / 10))


def led_flash_3(interval, pin):
    """
        *****注意*****
    関数を呼び出す際にはpin番号の値を与える事。
        ---GPIO出力---
    与えられたpin NOのGPIO PINのLEDを関数に与えられた値/10秒間点滅させる
    :param interval: int: 点滅間隔の設定。与えられたの/10感覚で点滅させる
    :param pin: int: LEDのGPIO PIN NO
    """
    LED1 = pin
    GPIO.pinMode(LED3, GPIO.OUTPUT)
    GPIO.digitalWrite(LED3, GPIO.HIGH)
    time.sleep(interval / 10)
    GPIO.digitalWrite(LED3, GPIO.LOW)
    time.sleep(interval / 10)


def led_flash_4(intterval, pin):
    """
        *****注意*****
    関数を呼び出す際にはpin番号の値を与える事。
    値を忘れるとエラーなのでtry文を忘れない。
        ---GPIO出力---
    与えられたpin NOのGPIO PINのLEDを関数に与えられた値/10秒間点滅させる
    :param interval: int: 点滅間隔の設定。与えられたの/10感覚で点滅させる
    :param pin: int: LEDのGPIO PIN NO
    """
    LED2 = pin
    GPIO.pinMode(LED4, GPIO.OUTPUT)
    GPIO.digitalWrite(LED4, GPIO.HIGH)
    time.sleep(intterval / 10)
    GPIO.digitalWrite(LED4, GPIO.LOW)
    time.sleep((intterval / 10))


def led_flash_5(intterval, pin):
    """
        *****注意*****
    関数を呼び出す際にはpin番号の値を与える事。
    値を忘れるとエラーなのでtry文を忘れない。
        ---GPIO出力---
    与えられたpin NOのGPIO PINのLEDを関数に与えられた値/10秒間点滅させる
    :param interval: int: 点滅間隔の設定。与えられたの/10感覚で点滅させる
    :param pin: int: LEDのGPIO PIN NO
    """
    LED2 = pin
    GPIO.pinMode(LED5, GPIO.OUTPUT)
    GPIO.digitalWrite(LED5, GPIO.HIGH)
    time.sleep(intterval / 10)
    GPIO.digitalWrite(LED5, GPIO.LOW)
    time.sleep((intterval / 10))


def led_flash_1and2(interval, pin1, pin2):
    """
        *****注意*****
    関数を呼び出す際にはpin番号の値を与える事。
        ---GPIO出力---
    与えられたpin NOのGPIO PINのLEDを関数に与えられた値/10秒間点滅させる
    :param interval: int: 点滅間隔の設定。与えられたの/10感覚で点滅させる
    :param pin1: int: 1つ目LEDの GPIO PIN NO
    :param pin2: int: 2つ目LEDの GPIO PIN NO
    """
    LED1 = pin1
    LED2 = pin2
    GPIO.pinMode(LED1, GPIO.OUTPUT)
    GPIO.pinMode(LED2, GPIO.OUTBoolPUT)
    GPIO.digitalWrite(LED1, GPIO.HIGH)
    GPIO.digitalWrite(LED2, GPIO.HIGH)
    time.sleep(interval / 10)
    GPIO.digitalWrite(LED1, GPIO.LOW)
    GPIO.digitalWrite(LED2, GPIO.LOW)
    time.sleep(interval / 10)


"""

スイッチ関数

"""


def push_sw_1(output):
    """
        *****注意*****
    関数を呼び出す際にはpin番号の値を与える事。
        ---GPIO入力---    
    関数に与えられた値のGPIOを使用でスイッチング。
    対応GPIOから1KΩの抵抗、スイッチでGNDへ戻す。
    ラズパイ内部のpullup抵抗に対応なのでスイッチが押されてない時はHIGH
    スイッチが押されるとLOW。
    押されているときはTrue、押されてないときはFalseを返す。
    :param output: int: スイッチのoutput用pin no
    :returns 
    """
    SW_PIN = output
    GPIO.pinMode(SW_PIN, GPIO.INPUT)
    GPIO.pullUpDnControl(SW_PIN, GPIO.PUD_UP)
    if (GPIO.digitalRead(SW_PIN) == GPIO.LOW):
        return True
    else:
        return False


def slide_sw_1(output):
    """
        *****注意*****
    関数を呼び出す際にはpin番号の値を与える事。
        ---GPIO入力---    
    関数に与えられた値のGPIOを使用でスイッチング。
    スライドスイッチなのでプルアッププルダウン抵抗はいらない
    ONのときはTrue、OFFのときはFalseを返す。
    :param output: int: スイッチのoutput用pin no
    :returns 
    """