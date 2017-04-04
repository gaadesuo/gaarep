# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/0 :10:57$'

import gpio_setting as GPIO

print(u"(´・ω・｀)ここは僕たちのスレだよ。きうり食べる？")

while True:
        if GPIO.slide_sw_1 == HIGH:
            print("彡(ﾟ)(ﾟ)なんやて！")
            break
        else:
            continue
