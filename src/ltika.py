# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/02 :20:36$'

import gpio_setting as LED_PIN

count = 0
interval = 0
pin1 = 0
pin2 = 0

print("""入力された時間の1/10秒ごと入力された回数LEDを点滅させます。
点滅は片方ずつ1回毎点滅し最後に両方同時に点滅で1ループです。""")
while True:
    try:
        interval = int(input("点滅間隔を数字で設定してください。(単位1/10秒) >>>"))
        count = int(input("繰り返す回数を数字で入れてください。 >>>"))
        break
    except:
        continue

for lp1 in range(count):
    LED_PIN.led1(interval, 14)
    LED_PIN.led2(interval, 15)
    LED_PIN.led1and2(interval, 14, 15)

print (u"終わり")
