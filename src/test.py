# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/02 :20:02$'

import time
import wiringpi as GPIO

# GPIOの初期化
GPIO.wiringPiSetupGpio()

"""

class

"""


class Led:
    """
    LEDの制御
    コンストラクタ引数はすべてintで(pin番号,モード,点灯時間,PWM割合100%,点滅回数)
    点灯時間は値の1/10(秒)
    デフォルト値:点灯時間1秒,pwm100%,回数1回
    PWM制御は0～100(%)それ以外で例外
    モードは1が点灯,2が点滅,0が消灯,それ以外で例外
    点滅時間は点灯は値で変わり消灯の時間は0.1秒の繰り返し
    """

    def __init__(self, pin, mode, timer=10, pwm=100, count=1):
        self.pin = pin
        self.mode = mode
        self.timer = timer
        self.pwm = pwm
        self.count = count

    def flash(self):
        """
        LEDの制御
        Led()で与えられた値にしたがってLEDを制御する
        コンストラクタ引数はすべてintで(pin番号,モード,点灯時間,PWM割合100%,点滅回数)
        """
        # pwmの値の確認
        if self.pwm < 0 or self.pwm > 101:
            raise PwmError("PWMの数値は0～100(%)です")

        # 複数かどうかの確認
        try:
            gpio_num = len(self.pin)

        # 以下LEDが単数指定
        except TypeError:
            # GPIOの設定
            LED1 = self.pin
            GPIO.pinMode(LED1, GPIO.OUTPUT)
            GPIO.softPwmCreate(LED1, 0, 100)

            # mode1 点灯
            if self.mode == 1:
                GPIO.softPwmWrite(LED1, self.pwm)
                time.sleep(self.timer / 10)

            # mode2 点滅
            elif self.mode == 2:
                for lp1 in range(self.count):
                    GPIO.softPwmWrite(LED1, self.pwm)
                    time.sleep(self.timer / 10)
                    GPIO.softPwmWrite(LED1, 0)
                    time.sleep(0.5)
                    print(1)

            # mode0 消灯
            elif self.mode == 0:
                GPIO.digitalWrite(LED1, GPIO.LOW)

            # 例外
            else:
                raise ModeError("モードは1:点灯 2:点滅 0:消灯 でそれ以外は例外です")


led100 = Led(12, 2, 10)
led50 = Led(12, 2, 20, 50, 2)
led30_HIGH = Led(12, 1, 30, 30, 3)
led_LOW = Led(12, 0)
led100.flash()
led50.flash()
led30_HIGH.flash()
led_LOW.flash()
