# -*- coding: utf-8 -*-

# mixi スイッチ回路実践source

import wiringpi as GPIO, time

# 押しボタンスイッチの使用するGPIO番号
PUSH_SW = 15

GPIO.wiringPiSetupGpio()
# （注）入力モード
GPIO.pinMode(PUSH_SW, GPIO.INPUT)

print(u"押すなよ。絶対に押すなよ！")
while True:
    if (GPIO.digitalRead(PUSH_SW) == GPIO.HIGH):
        print("YOU BAN")
        break

    else:
        time.sleep(0.1)
