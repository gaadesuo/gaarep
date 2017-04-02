# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/02 :20:02$'

import time
import wiringpi as GPIO

"""

GPIOの設定

"""
LED1 = 14
LED2 = 15

# GPIOの初期化
GPIO.wiringPiSetupGpio()

# GPIOの出力設定
GPIO.pinMode(LED1, GPIO.OUTPUT)
GPIO.pinMode(LED2, GPIO.OUTPUT)

"""

関数

"""


def led14(interval):
    """
    ---GPIO出力---
    GPIO PIN NO14のLEDを関数に与えられた値/10秒間点滅させる
    :param interval:int: 点滅間隔の設定。与えられたの/10感覚で点滅させる
    """
    GPIO.digitalWrite(LED1, GPIO.HIGH)
    time.sleep(interval / 10)
    GPIO.digitalWrite(LED1, GPIO.LOW)
    time.sleep(interval / 10)


def led15(intterval):
    """
    ---GPIO出力---
    GPIO PIN NO15のLEDを関数に与えられた値/10秒間点滅させる
    :param interval:int: 点滅間隔の設定。与えられたの/10感覚で点滅させる
    """
    GPIO.digitalWrite(LED2, GPIO.HIGH)
    time.sleep(intterval / 10)
    GPIO.digitalWrite(LED2, GPIO.LOW)
    time.sleep((intterval / 10))


def led14and15(interval):
    """
    ---GPIO出力---
    GPIO PIN NO14と15のLEDを共に関数に与えられた値/10秒間点滅させる
    :param interval:int: 点滅間隔の設定。与えられたの/10感覚で点滅させる
    """
    GPIO.digitalWrite(LED1, GPIO.HIGH)
    GPIO.digitalWrite(LED2, GPIO.HIGH)
    time.sleep(interval / 10)
    GPIO.digitalWrite(LED1, GPIO.LOW)
    GPIO.digitalWrite(LED2, GPIO.LOW)
    time.sleep(interval / 10)