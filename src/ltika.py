# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/02 :20:36$'

import gpio_setting as pin


def led_flash():
    """
    LEDの点滅制御設定を決めて、点滅させる
    """
    print("""入力された時間の1/10秒ごと入力された回数LEDを点滅させます。
    点滅は片方ずつ1回毎点滅し最後に両方同時に点滅で1ループです。""")
    while True:
        try:
            interval = int(input("点滅間隔を数字で設定してください。(単位1/10秒) >>>"))
            count = int(input("繰り返す回数を数字で入れてください。 >>>"))
            break
        except:
            continue

    led1 = pin.Led(12, 2, 5, 100, 1)
    led1.flash()

if __name__ == "__main__":
    led_flash()