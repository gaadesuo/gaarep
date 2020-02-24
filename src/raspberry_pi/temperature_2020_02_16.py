#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2020/02/16 09:05'

import RPi.GPIO as GPIO
import smbus
from time import sleep
from threading import Timer


def main():
    """
    2020/02/16
    ADT7410からの温度計測数値を13bit読み出しと16bit読み出し、どちらもテスト。

    2020/02/17
    4桁7segLEDに表記刺せるため13bit読み出しのみで運用。
    16bit読み出しをまとめ、行コメント化。
    16bit用デバッグプリントを削除。

    2020/02/18
    スイッチによるON OFF制御を追加。監視中のLED青を追加。

    2020/02/21
    温度監視を追加。
    エラー処理時のLEDを0.5秒で点滅をさせる処理を追加。

    2020/02/20
    ブザーを追加
    エラーリセットを追加
    """

    """
    初期設定
    """

    # pinの定義

    # スイッチ
    sw_black = 5
    sw_white = 6
    sw_red = 13

    # LED
    led_blue = 17
    led_red = 27

    # buzzer
    buzzer = 22

    # GPIOの設定

    GPIO.setmode(GPIO.BCM)
    # LEDへの出力
    GPIO.setup(led_blue, GPIO.OUT)
    GPIO.setup(led_red, GPIO.OUT)
    # 圧電ブザーへの出力
    GPIO.setup(buzzer, GPIO.OUT)
    # PWMの設定
    buzz_pwm = GPIO.PWM(buzzer, 244)
    buzz_pwm.start(0)

    # タクトスイッチからの入力
    # 内部プルアップを使用
    GPIO.setup(sw_black, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(sw_white, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(sw_red, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # adt7410の設定

    # コネクションオブジェクトの取得。
    bus = smbus.SMBus(1)
    adt7410_addr = 0x48
    adt7410_reg = 0x00
    # 下のconfは読み出しbitの設定場所。
    adt7410_conf = 0x03

    # 変数の代入

    # timer変数を定義
    delay_timer = None
    flash_on_timer = None
    flash_off_timer = None
    # 許容範囲の幅。±設定値の超えるとエラー判定
    tolerance = float(1)
    # ディレイフラグ
    delay_flag = 0
    # エラーフラグ
    error_flag = 0
    # LED点滅フラグ
    led_flash_flag = 0



    def error_check(m_temp, ref_temp, tol):
        """
        m_temp: 現在温度(float)
        ref_temp: 基準温度(float)
        tol: 許容範囲(float
        return: bool
        """
        if ((m_temp > (ref_temp + tol)) or (m_temp < (ref_temp - tol))):
            print("異常温度")
            return True
        else:
            print("正常温度")
            return False


    """
    本体
    """

    try:
        while True:

            # タクトスイッチ黒を押されたら監視開始
            # 監視中はLED青を点灯
            if GPIO.input(sw_black) == GPIO.LOW:
                GPIO.output(led_blue, GPIO.HIGH)

                # 監視立ち上がり判定のためNoneをプログラム開始時に代入
                reference_temp = None

                # タクトスイッチ白を押されるまで監視モード
                while GPIO.input(sw_white) == GPIO.HIGH:

                    """
                    読み出し
                    """

                    # メソッド configration_adt7410, 0x00 で13bit読み出し。
                    bus.write_word_data(adt7410_addr, adt7410_conf, 0x00)
                    thermo_date_13 = bus.read_word_data(adt7410_addr, adt7410_reg)
                    # print("スレーブの値 13bit {}".format(hex(thermo_date_13)))

                    """
                    # 16bit
                    # bus.write_word_data(adt7410_addr, adt7410_conf, 0x80)
                    # thermo_date_16 = bus.read_word_data(adt7410_addr, adt7410_reg)
                    # change_date_16 = (thermo_date_16 & 0xff00) >> 8 | (thermo_date_13 & 0xff) << 8
                    """

                    # 上位、下位byteの入れ替え。
                    # 上位1byteを8bit右へシフト、下位1byteを8bit左へシフト。
                    change_date_13 = (thermo_date_13 & 0xff00) >> 8 | (thermo_date_13 & 0xff) << 8
                    # print("上位、下位byteを並べ替えた後 13bit {}".format(hex(change_date_13)))
                    # print("2進数表記 13bit {}".format(bin(change_date_13)))

                    # 13bitを3bit右にシフト
                    change_date_13 = change_date_13 >> 3
                    # print("3bit移動後 13bit {}".format(bin(change_date_13)))
                    # 10進数で表記
                    # print("10進数表記 13bit {}".format(change_date_13))

                    # 実温度を出すための計算
                    monitoring_temp = change_date_13 / 16
                    print("温度 {}".format(monitoring_temp))

                    """
                    温度監視
                    """

                    # 監視立ち上がりの時の温度を基準温度として代入

                    if reference_temp is None:
                        reference_temp =  monitoring_temp
                        print("基準温度は {}℃".format(reference_temp))

                    # 基準温度±許容範囲を超えた状態が5秒続いた場合エラー処理
                    # 5秒以内に範囲内に戻った場合は5秒タイマーをキャンセルしてNoneに書き換え
                    # ディレイ処理はスレッドを生成

                    if error_check(monitoring_temp, reference_temp, tolerance) and delay_flag == 0:
                        if delay_timer is None:
                            delay_timer = Timer(5, GPIO.output, (led_red, GPIO.HIGH))
                            delay_timer.setDaemon(True)
                            delay_timer.start()
                            delay_flag = 1
                        # print("エラーディレイタイマ開始")
                    if error_check(monitoring_temp, reference_temp, tolerance) == False and delay_flag == 1:
                        delay_timer.cancel()
                        delay_timer = None
                        delay_flag = 0
                        # print("エラーディレイキャンセル")

                    """
                    エラー警告処理
                    """

                    # エラーディレイがキャンセルされなかった場合、エラー発生
                    # エラーリセット処理がされるかタクトスイッチ白が押されるまでブザーを鳴らし、とLED垢を点滅させる
                    # error_flag、led_flash_flagに1を代入
                    # ディレイ処理スレッドがNoneじゃなければスレッドが作成されているので
                    # 作成されたディレイ処理のスレッドをキャンセル
                    if GPIO.input(led_red) == 1:
                        error_flag = 1
                        led_flash_flag = 1
                        # print("LED点灯したのでスレッドキャンセル")
                        if delay_timer is not None:
                            delay_timer.cancel()
                        # ブザーが鳴ってないならブザーを鳴らす
                        if GPIO.input(buzzer) == 0:
                            # print("ブザーON")
                            buzz_pwm.ChangeDutyCycle(90)

                    # LED
                    # 点滅処理
                    # error_flagが立っていて温度が範囲外の時。
                    # LEDが点灯し、led_flash_flagが1の時は0.5秒ディレイ消灯スレッドを作成
                    # LEDが消灯し、led_flash_flagが0の時は0.5秒ディレイ点灯スレッドを作成
                    # 点灯消灯の切り替わりの立ち上がり管理は if 文と フラグ管理で行う
                    if error_flag == 1:
                        print(flash_on_timer)
                        print(flash_off_timer)
                        print(delay_timer)

                        if GPIO.input(led_red) == 1 and led_flash_flag == 1:
                            print("LED消灯ディレイ開始")
                            led_flash_flag = 0
                            if flash_off_timer is None:
                                flash_off_timer = Timer(0.5, GPIO.output, (27, GPIO.LOW))
                                flash_off_timer.setDaemon(True)
                                flash_off_timer.start()
                                flash_on_timer = None

                        elif GPIO.input(led_red) == 0 and led_flash_flag == 0:
                            print("LED点灯ディレイ開始")
                            if flash_on_timer is None:
                                led_flash_flag = 1
                                flash_on_timer = Timer(0.5, GPIO.output, (27, GPIO.HIGH))
                                flash_on_timer.setDaemon(True)
                                flash_on_timer.start()
                                flash_off_timer = None

                    """
                    エラーリセット処理
                    """

                    # エラーLEDとブザーの解除判定
                    # エラー警告時に現在温度が範囲内に戻っているときにリセットボタンを押すと
                    # LED ON OFFの切り替えディレイスレッドをキャンセルしてNoneに書き換え
                    # 開始ディレイスレッドもキャンセルしてNoneに書き換え
                    # ブザーのPWM制御を0にする。

                    if ((error_check(monitoring_temp, reference_temp, tolerance) == False) and error_flag == 1) and \
                            GPIO.input(sw_red) == GPIO.LOW:
                        error_flag = 0
                        led_flash_flag = 0

                        if flash_on_timer is not None:
                            flash_on_timer.cancel()
                            flash_on_timer.join()
                        if flash_off_timer is not None:
                            flash_off_timer.cancel()
                            flash_off_timer.join()
                        if delay_timer is not None:
                            delay_timer.cancel()
                            delay_timer.join()
                        flash_off_timer = None
                        flash_on_timer = None
                        delay_timer = None
                        buzz_pwm.ChangeDutyCycle(0)

                    sleep(0.5)

                # タクトスイッチ白を押されたらLEDとブザーを消す
                # ディレイタイマ用スレッドが生成されているときはキャンセル
                # 各フラグの初期化
                else:
                    GPIO.output(led_blue, GPIO.LOW)
                    GPIO.output(led_red, GPIO.LOW)
                    buzz_pwm.ChangeDutyCycle(0)
                    if error_flag == 1:
                        if flash_on_timer is not None:
                            print(flash_on_timer)
                            flash_on_timer.cancel()
                            flash_on_timer.join()
                        if flash_off_timer is not None:
                            print(flash_off_timer)
                            flash_off_timer.cancel()
                            flash_off_timer.join()
                        if delay_timer is not None:
                            delay_timer.cancel()
                            delay_timer.join()
                        flash_off_timer = None
                        flash_on_timer = None
                        delay_timer = None
                        buzz_pwm.ChangeDutyCycle(0)
                    delay_flag = 0
                    error_flag = 0
                    led_flash_flag = 0

            # 開始待ち中にタクトスイッチ赤を押されるとLEDを消灯してプログラム終了
            if GPIO.input(sw_red) == GPIO.LOW:
                break
            sleep(0.1)

    except KeyboardInterrupt:
        pass

    except AttributeError:
        pass
    
    GPIO.cleanup()


if __name__ == '__main__':
    main()