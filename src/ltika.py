# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/02 :20:36$'

import gpio_setting as pin
import time


def led_flash():
    """
    LEDの点滅制御設定を決めて、点滅させる
    """
    print("""入力された時間の1/10秒ごと入力された回数LEDを最後に点滅させます。
    点滅は片方ずつ1回毎点滅し最後に両方同時に点滅で1ループです。""")
    while True:
        try:
            interval = int(input("点滅間隔を数字で設定してください。(単位1/10秒) >>>"))
            count = int(input("最後に繰り返す回数を数字で入れてください。 >>>"))
            break
        except:
            continue

    brightness = [100, 60, 20, 0]

    for bri in brightness:
        led_1_up = pin.Led(12, 1, interval, bri)
        led_1_up.flash()
        time.sleep(0.5)
        led_2_up = pin.Led(5, 1, interval, bri)
        led_2_up.flash()
        time.sleep(0.5)
        led_3_up = pin.Led(6, 1, interval, bri)
        led_3_up.flash()
        time.sleep(0.5)
        led_4_up = pin.Led(13, 1, interval, bri)
        led_4_up.flash()
        time.sleep(0.5)
        led_5_up = pin.Led(19, 1, interval, bri)
        led_5_up.flash()
        time.sleep(0.5)

    led_all = pin.Led((12, 5, 6, 13, 19), 2, interval, 100, count)
    led_all.flash()

if __name__ == "__main__":
    led_flash()