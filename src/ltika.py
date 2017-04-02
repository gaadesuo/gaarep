# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/02 :20:36$'

import pin14_15led as LED

count = 0
interval = 0

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
    LED.led14(interval)
    LED.led15(interval)
    LED.led14and15(interval)

print (u"終わり")
