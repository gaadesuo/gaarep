# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/02 :20:02$'

import time
import wiringpi as GPIO

"""

beepクラス

"""


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
        GPIO.wiringPiSetupGpio()
        GPIO.softToneCreate(self.pin)
        x = self.onpu
        y = self.melody
        z = self.interval
        for (oto, nagasa, yasumi) in zip(x, y, z):
            GPIO.sofltToneWrite(self.pin, oto)
            print(self.pin, oto, nagasa, yasumi)
            time.sleep(nagasa / 10)
            GPIO.sofltToneWrite(self.pin, oto)
            time.sleep(yasumi / 10)


if __name__ == "__main__":

    BUZ = Buzzer(26, 262 , 10, 11)
    BUZ.beep()