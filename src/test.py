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
    *** 注意 ***
    使用の際は実行側でGPIOの初期設定が必要
    ************
    
    圧電ブザーの制御
    コンストラクタ引数はすべてintで書式は以下(self)は除く
    変数名 = Buzzer(pin, onpu, melody, interval):
    :param pin:int: GPIO PIN 番号
    :param onpu: int:圧電ブザーの音階周波数。音階は下記
    :param melody: int: 圧電ブザーを鳴らす時間
    :param interval: int: 鳴らした後の休める時間デフォルト値は0(休みなし)
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
        
    時間設定は値の/10秒
    その間高圧ブザーを鳴らす。停止はメロディラインを作るときに必要
    
    """
    def __init__(self, pin, onpu, melody, interval=0):
        self.pin = pin
        self.onpu = onpu
        self.melody = melody
        self.interval = interval

    def beep(self):
        """
        圧電ブザーの制御
        Buzzer()に与えられた値によって圧電ブザーを鳴らす
        呼び出す場合にモジュール名はいらない
        変数名.beep
        """
        # 値の確認
        if self.onpu < 0:
            raise FrequencyError("周波数の値がマイナスです")
        if self.melody < 0:
            raise TimeError("時間の値がマイナスです")
        GPIO.softToneCreate(self.pin)

        GPIO.softToneWrite(self.pin, self.onpu)
        time.sleep(self.melody / 10)
        GPIO.softToneWrite(self.pin, self.onpu)
        if self.interval > 0:
            time.sleep(self.interval / 10)
        elif self.interval == 0:
            pass
        else:
            raise TimeError("時間の値がマイナスです")


if __name__ == "__main__":

    # GPIOの初期化
    GPIO.wiringPiSetupGpio()

    BUZ = Buzzer(26, 262, 10, 1)
    re = Buzzer(26, 815, 10, 1)
    BUZ.beep()
    re.beep()