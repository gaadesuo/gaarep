# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/0 :10:57$'

import gpio_setting as GPIO

print(u"押すなよ。絶対に押すなよ！")
while True:
    if GPIO.push_sw_1(12):
        break
    else:
        continue
print("YOU BAN")