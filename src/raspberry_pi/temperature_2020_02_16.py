#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2020/02/16 09:05'

import RPi.GPIO as GPIO
import smbus
from time import sleep
from threading import Timer
import datetime


def read_temp():
    """

    """


def error_check(m_temp, ref_temp, tol):
    """
    m_temp: 現在温度(float)
    ref_temp: 基準温度(float)
    tol: 許容範囲(float
    return: bool

    現在温度が範囲内に入っているかを判定。
    入っていればTrue、外れてればFalseを返す。
    """
    if ((m_temp > (ref_temp + tol)) or (m_temp < (ref_temp - tol))):
        return True
    else:
        return False


def led_flash(sw_r, led_r):
    """
    sw_r: スイッチ赤のGPIO番号
    led_r: LED赤のGPIO番号

    スイッチ赤が押されるまで0.5秒周期でLEDを点滅させる。
    スイッチの判定はLED点灯前と消灯時に行う
    """
    while True:
        if GPIO.input(sw_r, GPIO.HIGH):
            break
        else:
            GPIO.output(led_r, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led_r, GPIO. LOW)
        if GPIO.input(sw_r, GPIO.HIGH):
            break
        else:
            sleep(0.5)


def log_write(err_count):
    """
    ログ取得

    return: エラーカウントを1増やして返す
    ログファイルに現在時刻を書き込んでエラーカウントを1増やす
    """
    err_count += 1
    print("エラーカウント+1して {} になった".format(err_count))

    # エラー時間のログファイルへの書き出し
    time_log = datetime.datetime.now()
    time_log = time_log.strftime('"%Y-%m-%d %H:%M:%S"')
    print("エラー時刻 {}".format(time_log))
    with open("log.txt", "a", encoding="utf_8") as log_w:
        log_w.write(time_log + "\n")
    log_w.close()

    return err_count

def main():

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

    # 許容範囲の幅。±設定値の超えるとエラー判定
    tolerance = float(1)
    # ディレイフラグ
    delay_flag = 0
    # エラーフラグ
    error_flag = 0
    # LED点滅フラグ
    led_flash_flag = 0
    # errorカウンター
    error_counter = 0

    """
    本体
    """

    try:
        while True:

            # タクトスイッチ黒を押されたら監視開始
            # 監視中はLED青を点灯
            if GPIO.input(sw_black) == GPIO.LOW:
                GPIO.output(led_blue, GPIO.HIGH)

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
                        reference_temp = monitoring_temp
                        print("基準温度は {}℃".format(reference_temp))

                    # デバッグ用 温度判定表示
                    if error_check(monitoring_temp, reference_temp, tolerance):
                        print("異常温度")
                    else:
                        print("正常温度")

                    # 基準温度±許容範囲を超えた状態が5秒続いた場合エラー処理
                    # 5秒以内に範囲内に戻った場合は5秒タイマーをキャンセルしてNoneに書き換え
                    # ディレイ処理はスレッドを生成

                    if error_check(monitoring_temp, reference_temp,
                                   tolerance) and delay_flag == 0 and led_flash_flag == 0:
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
                    # 立ち上がり(error_flagが0の時)ログを書き込み、エラーカウントを+= 1してerroe_flagに1を代入
                    # エラーリセット処理がされるかタクトスイッチ白が押されるまでブザーを鳴らし、とLED垢を点滅させる
                    # error_flag、led_flash_flagに1を代入
                    # ディレイ処理スレッドがNoneじゃなければスレッドが作成されているので
                    # 作成されたディレイ処理のスレッドをキャンセル
                    if GPIO.input(led_red) == 1 and led_flash_flag == 0 and delay_flag == 1:
                        if error_flag == 0:
                            """
                            ログ取得
                            """
                            error_counter = log_write(error_counter)

                            error_flag = 1
                        led_flash_flag = 1
                        # print("LED点灯したのでスレッドキャンセル")
                        if delay_timer is not None:
                            delay_timer.cancel()
                        # ブザーが鳴ってないならブザーを鳴らす
                        if GPIO.input(buzzer) == 0:
                            # print("ブザーON")
                            buzz_pwm.ChangeDutyCycle(90)



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