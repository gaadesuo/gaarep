# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/0 :10:57$'

import gpio_setting as GPIO
import ltika

print(u"スイッチを押すと8LED点滅の設定が始まります")
while True:
    if GPIO.push_sw_1(26):
        break
    else:
        continue

ltika.led_flash()
