# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/02 :20:02$'

import time
import wiringpi as GPIO

"""

LEDクラス

"""


class Led:
    """
    *** 注意 ***
    使用の際は実行側でGPIOの初期設定が必要
    ************
    LEDの制御
    コンストラクタ引数はすべてintで書式は以下(self)は除く
    変数名 = Led(pin, mode, timer, pwm, count):
    :param pin: int: GPIO PIN番号 
    :param mode: int: 点灯の設定
    :param timer: int: 点灯時間
    :param pwm: int: PWM制御の割合
    :param count: int: 繰り返し回数

    点灯時間は値の1/10(秒)
    点滅時間は点灯は値で変わり消灯の時間は0.5秒の繰り返し
    pinはタプルもしくはリストで同時複数制御設定。2～5個の間で対応。範囲外で例外処理
    PWM制御は0～100(%)それ以外で例外処理
    モードは1が点灯,2が点滅,0が消灯,それ以外で例外処理
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
        呼び出す場合はモジュール名はいらない。
        変数名.flash()
        """
        # pwmの値の確認
        if self.pwm < 0 or self.pwm > 101:
            raise PwmError("PWMの数値は0～100(%)です")

        # GPIOの複数かどうかの確認
        try:
            gpio_num = len(self.pin)

            # LED2つ処理
            if gpio_num == 2:
                # GPIOの設定
                LED1 = self.pin[0]
                LED2 = self.pin[1]
                GPIO.pinMode(LED1, GPIO.OUTPUT)
                GPIO.pinMode(LED2, GPIO.OUTPUT)
                GPIO.softPwmCreate(LED1, 0, 100)
                GPIO.softPwmCreate(LED2, 0, 100)

                # mode1 点灯
                if self.mode == 1:
                    GPIO.softPwmWrite(LED1, self.pwm)
                    GPIO.softPwmWrite(LED2, self.pwm)
                    time.sleep(self.timer / 10)

                # mode2 点滅
                elif self.mode == 2:
                    for lp1 in range(self.count):
                        GPIO.softPwmWrite(LED1, self.pwm)
                        GPIO.softPwmWrite(LED2, self.pwm)
                        time.sleep(self.timer / 10)
                        GPIO.softPwmWrite(LED1, 0)
                        GPIO.softPwmWrite(LED2, 0)
                        time.sleep(0.5)

                # mode0 消灯
                elif self.mode == 0:
                    GPIO.digitalWrite(LED1, GPIO.LOW)
                    GPIO.digitalWrite(LED2, GPIO.LOW)

                # mode例外
                else:
                    raise ModeError("モードは1:点灯 2:点滅 0:消灯 でそれ以外は例外です")

            # LED3つ処理
            elif gpio_num == 3:
                # GPIOの設定
                LED1 = self.pin[0]
                LED2 = self.pin[1]
                LED3 = self.pin[2]
                GPIO.pinMode(LED1, GPIO.OUTPUT)
                GPIO.pinMode(LED2, GPIO.OUTPUT)
                GPIO.pinMode(LED3, GPIO.OUTPUT)
                GPIO.softPwmCreate(LED1, 0, 100)
                GPIO.softPwmCreate(LED2, 0, 100)
                GPIO.softPwmCreate(LED3, 0, 100)

                # mode1 点灯
                if self.mode == 1:
                    GPIO.softPwmWrite(LED1, self.pwm)
                    GPIO.softPwmWrite(LED2, self.pwm)
                    GPIO.softPwmWrite(LED3, self.pwm)
                    time.sleep(self.timer / 10)

                # mode2 点滅
                elif self.mode == 2:
                    for lp1 in range(self.count):
                        GPIO.softPwmWrite(LED1, self.pwm)
                        GPIO.softPwmWrite(LED2, self.pwm)
                        GPIO.softPwmWrite(LED3, self.pwm)
                        time.sleep(self.timer / 10)
                        GPIO.softPwmWrite(LED1, 0)
                        GPIO.softPwmWrite(LED2, 0)
                        GPIO.softPwmWrite(LED3, 0)
                        time.sleep(0.5)

                # mode0 消灯
                elif self.mode == 0:
                    GPIO.digitalWrite(LED1, GPIO.LOW)
                    GPIO.digitalWrite(LED2, GPIO.LOW)
                    GPIO.digitalWrite(LED3, GPIO.LOW)

                # mode例外
                else:
                    raise ModeError("モードは1:点灯 2:点滅 0:消灯 でそれ以外は例外です")

            # LED4つ処理
            elif gpio_num == 4:
                # GPIOの設定
                LED1 = self.pin[0]
                LED2 = self.pin[1]
                LED3 = self.pin[2]
                LED4 = self.pin[3]
                GPIO.pinMode(LED1, GPIO.OUTPUT)
                GPIO.pinMode(LED2, GPIO.OUTPUT)
                GPIO.pinMode(LED3, GPIO.OUTPUT)
                GPIO.pinMode(LED4, GPIO.OUTPUT)
                GPIO.softPwmCreate(LED1, 0, 100)
                GPIO.softPwmCreate(LED2, 0, 100)
                GPIO.softPwmCreate(LED3, 0, 100)
                GPIO.softPwmCreate(LED4, 0, 100)

                # mode1 点灯
                if self.mode == 1:
                    GPIO.softPwmWrite(LED1, self.pwm)
                    GPIO.softPwmWrite(LED2, self.pwm)
                    GPIO.softPwmWrite(LED3, self.pwm)
                    GPIO.softPwmWrite(LED4, self.pwm)
                    time.sleep(self.timer / 10)

                # mode2 点滅
                elif self.mode == 2:
                    for lp1 in range(self.count):
                        GPIO.softPwmWrite(LED1, self.pwm)
                        GPIO.softPwmWrite(LED2, self.pwm)
                        GPIO.softPwmWrite(LED3, self.pwm)
                        GPIO.softPwmWrite(LED4, self.pwm)
                        time.sleep(self.timer / 10)
                        GPIO.softPwmWrite(LED1, 0)
                        GPIO.softPwmWrite(LED2, 0)
                        GPIO.softPwmWrite(LED3, 0)
                        GPIO.softPwmWrite(LED4, 0)
                        time.sleep(0.5)

                # mode0 消灯
                elif self.mode == 0:
                    GPIO.digitalWrite(LED1, GPIO.LOW)
                    GPIO.digitalWrite(LED2, GPIO.LOW)
                    GPIO.digitalWrite(LED3, GPIO.LOW)
                    GPIO.digitalWrite(LED4, GPIO.LOW)

                # mode例外
                else:
                    raise ModeError("モードは1:点灯 2:点滅 0:消灯 でそれ以外は例外です")

            # LED5つ処理
            elif gpio_num == 5:
                # GPIOの設定
                LED1 = self.pin[0]
                LED2 = self.pin[1]
                LED3 = self.pin[2]
                LED4 = self.pin[3]
                LED5 = self.pin[4]
                GPIO.pinMode(LED1, GPIO.OUTPUT)
                GPIO.pinMode(LED2, GPIO.OUTPUT)
                GPIO.pinMode(LED3, GPIO.OUTPUT)
                GPIO.pinMode(LED4, GPIO.OUTPUT)
                GPIO.pinMode(LED5, GPIO.OUTPUT)
                GPIO.softPwmCreate(LED1, 0, 100)
                GPIO.softPwmCreate(LED2, 0, 100)
                GPIO.softPwmCreate(LED3, 0, 100)
                GPIO.softPwmCreate(LED4, 0, 100)
                GPIO.softPwmCreate(LED5, 0, 100)

                # mode1 点灯
                if self.mode == 1:
                    GPIO.softPwmWrite(LED1, self.pwm)
                    GPIO.softPwmWrite(LED2, self.pwm)
                    GPIO.softPwmWrite(LED3, self.pwm)
                    GPIO.softPwmWrite(LED4, self.pwm)
                    GPIO.softPwmWrite(LED5, self.pwm)
                    time.sleep(self.timer / 10)

                # mode2 点滅
                elif self.mode == 2:
                    for lp1 in range(self.count):
                        GPIO.softPwmWrite(LED1, self.pwm)
                        GPIO.softPwmWrite(LED2, self.pwm)
                        GPIO.softPwmWrite(LED3, self.pwm)
                        GPIO.softPwmWrite(LED4, self.pwm)
                        GPIO.softPwmWrite(LED5, self.pwm)
                        time.sleep(self.timer / 10)
                        GPIO.softPwmWrite(LED1, 0)
                        GPIO.softPwmWrite(LED2, 0)
                        GPIO.softPwmWrite(LED3, 0)
                        GPIO.softPwmWrite(LED4, 0)
                        GPIO.softPwmWrite(LED5, 0)
                        time.sleep(0.5)

                # mode0 消灯
                elif self.mode == 0:
                    GPIO.digitalWrite(LED1, GPIO.LOW)
                    GPIO.digitalWrite(LED2, GPIO.LOW)
                    GPIO.digitalWrite(LED3, GPIO.LOW)
                    GPIO.digitalWrite(LED4, GPIO.LOW)
                    GPIO.digitalWrite(LED5, GPIO.LOW)
                # mode例外
                else:
                    raise ModeError("モードは1:点灯 2:点滅 0:消灯 でそれ以外は例外です")
            # 2~5本以外の設定は例外処理
            else:
                raise Pin_numsError("pin設定を複数にするときは2～5個までの範囲で設定してください")

        # Typeエラーがでたのでpinは単数指定
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

            # mode0 消灯
            elif self.mode == 0:
                GPIO.digitalWrite(LED1, GPIO.LOW)

            # Mode例外
            else:
                raise ModeError("モードは1:点灯 2:点滅 0:消灯 でそれ以外は例外です")


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


"""

スイッチ関数

"""


def push_sw_1(output):
    """
        *****注意*****
    関数を呼び出す際の引数はpin番号の値を与える事。
        ---GPIO入力---    
    関数に与えられた値のGPIOを使用でスイッチング。
    対応GPIOから1KΩの抵抗、スイッチでGNDへ戻す。
    ラズパイ内部のpullup抵抗に対応なのでスイッチが押されてない時はHIGH
    スイッチが押されるとLOW。
    押されているときはTrue、押されてないときはFalseを返す。
    :param output: int: スイッチのoutput用pin no
    :returns bool
    """
    SW_PIN = output
    GPIO.pinMode(SW_PIN, GPIO.INPUT)
    GPIO.pullUpDnControl(SW_PIN, GPIO.PUD_UP)
    if GPIO.digitalRead(SW_PIN) == GPIO.LOW:
        return True
    else:
        return False


def slide_sw_1(output):
    """
        *****注意*****
    関数を呼び出す際にはpin番号の値を与える事。
        ---GPIO入力---    
    関数に与えられた値のGPIOを使用でスイッチング。
    スライドスイッチなのでプルアッププルダウン抵抗はいらない
    ONのときはTrue、OFFのときはFalseを返す。
    :param output: int: スイッチのoutput用pin no
    :returns bool
    """
    SW_PIN = output
    GPIO.pinMode(SW_PIN, GPIO.INPUT)
    if GPIO.digitalRead(SW_PIN) == GPIO.HIGH:
        return True
    else:
        return False