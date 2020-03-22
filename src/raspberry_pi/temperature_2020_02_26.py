#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2020/02/16 09:05'

import RPi.GPIO as GPIO
import smbus
from time import sleep
import threading
import queue
import datetime

# global変数
error_flag = False
timer_count = 0

def temp_read(sw_w, r_temp, interval_time):
    """
    sw_w : タクトスイッチ白のGPIO番号 (int)
    r_temp : 読み込んだ温度を渡す(float)
    intv_time : 監視の感覚時間

    タクトスイッチ黒を押されてから、タクトスイッチ白を押されるまで処理を行う。
    温度センサモジュールから温度を読み込み。
    温度を小数点第一位まで求めてmonitoring関数に渡す。
    """

    # adt7410の設定
    # コネクションオブジェクトの取得。
    bus = smbus.SMBus(1)
    adt7410_addr = 0x48
    adt7410_reg = 0x00
    # 下のconfは読み出しbitの設定場所。
    adt7410_conf = 0x03

    print("*** 温度読み込み開始 ***")

    # タクトスイッチ白を押されるまで監視。
    while GPIO.input(sw_w) == GPIO.HIGH:
        # メソッド configration_adt7410, 0x00 で13bit読み出し。
        bus.write_word_data(adt7410_addr, adt7410_conf, 0x00)
        inp_temp = bus.read_word_data(adt7410_addr, adt7410_reg)

        # 上位、下位byteの入れ替え。
        # 上位1byteを8bit右へシフト、下位1byteを8bit左へシフト。
        shift_num = (inp_temp & 0xff00) >> 8 | (inp_temp & 0xff) << 8
        # 3bit右にシフト
        shift_num = shift_num >> 3
        # 実温度を出すための計算
        temp_num = shift_num / 16
        # 小数点第一位で丸める
        temp_num = round(temp_num, 1)
        # print("現在温度 {}".format(temp_num))

        # キューとして温度を渡す
        r_temp.put(temp_num)

        sleep(interval_time)

    print("*** 温度読み込み終了 ***")
    # タクトスイッチ白を押されたら終了コードとして65535を送る
    r_temp.put(65535)


def monitoring(sw_w, m_temp, lim_num, intval_time, delay):
    """
    sw_w : タクトスイッチ白のGPIO番号 (int)
    m_temp : 受け取った温度の値(float)
    lim_num : 上下限の幅の値(float)
    error_def : エラースレッド
    intv_time : 監視の感覚時間
    delay : 上下限超えてからエラー発生までのディレイタイム(単位s)

    温度センサから温度を受け取ってからタクトスイッチ白を押されるまで処理を行う。
    現在温度を受け取り基準温度を超えているかを判定。
    上下限の幅の値は本体で定義。
    基準温度は初期動作時の温度を代入する。
    上下限の幅を超えた時間をカウント、規定時間を超えたらイベントを渡す。
    """
    global error_flag
    global timer_count
    print("*** 温度監視開始 ***")

    # ディレイタイムカウントを計算
    delay_cal = delay * (1 / intval_time)
    # 最初に渡された温度を基準温度に入れる
    criteria_temp = m_temp.get()

    # タクトスイッチ白を押されるまで温度の判定
    while GPIO.input(sw_w) == GPIO.HIGH:
        # print(threading.enumerate())
        # 現在温度の代入
        current_temp = m_temp.get()
        # 終了コードの65535が入ると終了。
        if current_temp == 65535:
            break
        print("基準温度: {} 現在温度: {}".format(criteria_temp, current_temp))

        # 温度監視部
        while current_temp >= criteria_temp + lim_num:
            timer_count += 1
            current_temp = m_temp.get()
            # 終了コードの65535が入ると終了。
            if current_temp == 65535:
                break
            print("error! 基準温度: {} 現在温度: {} エラーカウント:{}"
                  .format(criteria_temp, current_temp, timer_count))
            # カウントを超えた初回のみエラーフラグを立てる。
            if timer_count > delay_cal and error_flag == False:
                # print("エラーを渡す")
                error_flag = True

        # 範囲内に戻ったらカウントを0にしてフラグを戻す。
        else:
            timer_count = 0

    print("*** 温度監視終了 ***")


def error_pro(sw_w, sw_r, err_count, buz_pwm):
    """
    sw_w : タクトスイッチ白のGPIO番号
    sw_r : タクトスイッチ赤のGPIO番号。
    err_temp : 現在温度の値。
    err_count : エラーカウンタ。
    buz_pwm : ブザーのPWMの値

    エラー時にスレッドを開始。
    開始時にエラーカウントを数えて、ログファイルへログの書き込み。
    """
    global error_flag
    global timer_count
    print("***エラースレッド開始***")

    while True:
        sleep(0.1)
        if error_flag:
            err_count += 1
            print("エラーカウント+1して {} になった".format(err_count))
            # ログファイルへログを書き込む
            time_log = datetime.datetime.now()
            time_log = time_log.strftime('"%Y-%m-%d %H:%M:%S"')
            print("エラー時刻 {}".format(time_log))
            with open("log.txt", "a", encoding="utf_8") as log_write:
                log_write.write(time_log + "\n")
            log_write.close()

            # ブザー吹鳴
            buz_pwm.ChangeDutyCycle(90)

            # エラー処理後は温度が正常に戻りタクトスイッチ赤を押されるか、白を押されるまでループ
            while True:
                sleep(0.1)
                if (timer_count == 0 and GPIO.input(sw_r) == GPIO.LOW) or GPIO.input(sw_w) == GPIO.LOW:
                    buz_pwm.ChangeDutyCycle(0)
                    error_flag = False
                    break

        if GPIO.input(sw_w) == GPIO.LOW:
            break

    print("*** エラースレッド終了 ***")

def led_flash(sw_w, led_r, led_f_time):
    """
    sw_w : タクトスイッチ白のGPIO番号
    led_r : LED赤のGPIO番号
    led_f_time : LEDの点滅時間(単位s)

    エラー発生時に赤色LEDを設定時間でON OFFさせる。
    """
    led_count = 0
    print("*** LEDスレッド開始***")
    global error_flag
    while True:
        if error_flag:
            # 0.1秒ごとカウント
            led_count += 0.1
            # print("LED点滅カウント {}".format(led_count))

            # 点滅設定時間以下の立ち上がり時にLEDをONする。
            if led_count <= led_f_time and GPIO.input(led_r) == GPIO.LOW:
                GPIO.output(led_r, GPIO.HIGH)
            # 点滅設定時間を超えたらLEDをOFFする。
            # 点滅カウントが2倍(繰り返し終了時)にカウントをリセット。
            elif led_count > led_f_time:
                GPIO.output(led_r, GPIO.LOW)
                if (led_f_time * 2) <= led_count:
                    led_count = 0

        # エラーが取り除かれるとカウントを初期化して赤LEDを消す。
        else:
            led_count = 0
            GPIO.output(led_r, GPIO.LOW)

        sleep(0.1)

        # タクトスイッチ白を押されると終了。
        if GPIO.input(sw_w) == GPIO.LOW:
            break
    print("*** LEDスレッド終了 ***")


def main():
    """
    本体
    """

    """
    変数定義
    """

    up_low_limit = 3.0 # 温度の上下限の幅
    delay_time = 5 # 上下限を超えてエラーをp出すまでのディレイタイム(単位s)
    interval_time = 0.5 # 監視の時間間隔
    led_flash_time = 0.5 # LEDのON OFF繰り返し時間(単位s)
    error_count = 0

    """
    pinの定義
    """
    # スイッチ
    sw_black = 5
    sw_white = 6
    sw_red = 13

    # LED
    led_blue = 17
    led_red = 27

    # buzzer
    buzzer = 22

    """
    GPIOの設定
    """

    # GPIO_PINの設定
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

    """
    マルチスレッド関連の設定
    """
    # キューの定義
    monitoring_temp = queue.Queue()
    # スレッドの定義
    thread_error = threading.Thread(target=error_pro, args=(sw_white, sw_red , error_count, buzz_pwm))
    thread_temp = threading.Thread(target=temp_read, args=(sw_white, monitoring_temp, interval_time))
    thread_monitoring = threading.Thread(target=monitoring,
                                         args=(sw_white, monitoring_temp, up_low_limit, interval_time,
                                               delay_time))
    thread_led = threading.Thread(target=led_flash, args=(sw_white, led_red, led_flash_time))

    """
    メイン処理
    """
    try:

        # タクトスイッチ黒を押されるまで入力待ち
        while GPIO.input(sw_black) == GPIO.HIGH:
            sleep(0.1)
        # 監視開始
        GPIO.output(led_blue, GPIO.HIGH)
        thread_temp.start()
        thread_monitoring.start()
        thread_error.start()
        thread_led.start()

        # タクトスイッチ白を押されるとGPIOをクリーンアップして終了
        while GPIO.input(sw_white) == GPIO.HIGH:
            sleep(0.1)
        else:
            GPIO.output(led_blue, GPIO.LOW)
            print(" *** 終了処理開始 *** ")
            error_count = 0
            buzz_pwm.ChangeDutyCycle(0)
            sleep(2)
            GPIO.cleanup()
            print(" *** 終了処理完了 ***")

    except KeyboardInterrupt:
        GPIO.cleanup()



if __name__ == '__main__':
    main()