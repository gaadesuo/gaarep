# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/02 :20:02$'

import time
import wiringpi as GPIO

"""

beepクラス

"""
# GPIOの初期化
GPIO.wiringPiSetupGpio()

class Buzzer:
    """

    :param onpu: 
    :param melody: 
    :param interval: 
            # -----音階周波数-----
        低シ = 247
        ド = 262
        レ = 294
        ミ = 330
        ファ = 349
        ソ = 392
        ラ = 440
        シ = 494
        高ド = 523
        morse = 815
    """
    def __init__(self,pin, onpu, melody, interval):
        self.pin = pin
        self.onpu = onpu
        self.melody = melody
        self.interval = interval

    def beep(self):
        """

        """
        GPIO.softToneCreate(self.pin)

        GPIO.softToneWrite(self.pin, self.onpu)
        time.sleep(self.melody / 10)
        GPIO.softToneWrite(self.pin, self.onpu)
        time.sleep(self.interval / 10)


if __name__ == "__main__":

    BUZ = Buzzer(26, 262, 10, 1)
    re = Buzzer(26, 815, 10, 1)
    BUZ.beep()
    re.beep()