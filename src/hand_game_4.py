# -*- coding: utf-8 -*-
import random
import time
import wiringpi as GPIO


#-----   GPIO設定   -----


PUSH_SW_GUU   = 14        #PIN NO  8
PUSH_SW_TYOKI = 15        #PIN NO 10
PUSH_SW_PAA   = 18        #PIN NO 12

LED_JYAN      = 23        #PIN NO 16
LED_AIKO      = 24        #PIN NO 18

LED_M_GUU     = 17        #PIN NO 11
LED_M_TYOKI   = 27        #PIN NO 13
LED_M_PAA     = 22        #PIN NO 15

LED_C_GUU     = 10        #PIN NO 19
LED_C_TYOKI   =  9        #PIN NO 21
LED_C_PAA     = 11        #PIN NO 23

LED_M_WIN_1   = 25        #PIN NO 22
LED_M_WIN_2   =  8        #PIN NO 24
LED_M_WIN_3   =  7        #PIN NO 26

LED_C_WIN_1   = 16        #PIN NO 36
LED_C_WIN_2   = 20        #PIN NO 38
LED_C_WIN_3   = 21        #PIN NO 40



GPIO.wiringPiSetupGpio()

GPIO.pinMode( PUSH_SW_GUU, GPIO.INPUT)        #入力注意
GPIO.pinMode( PUSH_SW_TYOKI, GPIO.INPUT)      #入力注意
GPIO.pinMode( PUSH_SW_PAA, GPIO.INPUT)        #入力注意

GPIO.pinMode( LED_JYAN, GPIO.OUTPUT)
GPIO.pinMode( LED_AIKO, GPIO.OUTPUT)

GPIO.pinMode( LED_M_GUU, GPIO.OUTPUT)
GPIO.pinMode( LED_M_TYOKI, GPIO.OUTPUT)
GPIO.pinMode( LED_M_PAA, GPIO.OUTPUT)

GPIO.pinMode( LED_C_GUU, GPIO.OUTPUT)
GPIO.pinMode( LED_C_TYOKI, GPIO.OUTPUT)
GPIO.pinMode( LED_C_PAA, GPIO.OUTPUT)

GPIO.pinMode( LED_M_WIN_1, GPIO.OUTPUT)
GPIO.pinMode( LED_M_WIN_2, GPIO.OUTPUT)
GPIO.pinMode( LED_M_WIN_3, GPIO.OUTPUT)

GPIO.pinMode( LED_C_WIN_1, GPIO.OUTPUT)
GPIO.pinMode( LED_C_WIN_2, GPIO.OUTPUT)
GPIO.pinMode( LED_C_WIN_3, GPIO.OUTPUT)


#-----   初期化とループ開始   -----


print(u"ゲームを開始します")
win  = 0
lose = 0
aiko = 0
GPIO.digitalWrite( LED_C_WIN_1, GPIO.LOW)
GPIO.digitalWrite( LED_C_WIN_2, GPIO.LOW)
GPIO.digitalWrite( LED_C_WIN_3, GPIO.LOW)
GPIO.digitalWrite( LED_M_WIN_1, GPIO.LOW)
GPIO.digitalWrite( LED_M_WIN_2, GPIO.LOW)
GPIO.digitalWrite( LED_M_WIN_3, GPIO.LOW)
GPIO.digitalWrite( LED_JYAN, GPIO.LOW)

while True:
    GPIO.digitalWrite( LED_M_GUU, GPIO.LOW)
    GPIO.digitalWrite( LED_M_TYOKI, GPIO.LOW)
    GPIO.digitalWrite( LED_M_PAA, GPIO.LOW)
    GPIO.digitalWrite( LED_C_GUU, GPIO.LOW)
    GPIO.digitalWrite( LED_C_TYOKI, GPIO.LOW)
    GPIO.digitalWrite( LED_C_PAA, GPIO.LOW)
    man = 0


    #-----   じゃんけんあいこLED点灯   -----


    if aiko == 1:
        for lp01 in range(2):
            GPIO.digitalWrite( LED_AIKO, GPIO.HIGH)             #あいこでしょに合わせて3回光らせる
            time.sleep(0.5)                                     #3回目は入力されるまで光らせる
            GPIO.digitalWrite( LED_AIKO, GPIO.LOW)
            time.sleep(0.2)
        GPIO.digitalWrite( LED_AIKO, GPIO.HIGH)
        aiko = 0
    else:
        for lp02 in range(2):
            GPIO.digitalWrite( LED_JYAN, GPIO.HIGH)             #じゃんけんも同上
            time.sleep(0.5)
            GPIO.digitalWrite( LED_JYAN, GPIO.LOW)
            time.sleep(0.2)
        GPIO.digitalWrite( LED_JYAN, GPIO.HIGH)


    #-----   人間入力   -----


    while man == 0:

        if (GPIO.digitalRead(PUSH_SW_GUU) == GPIO.HIGH):        #※以下3つGPIO入力。注意、確認
            man = 1                                             #グーは1 チョキは2 パーは3
        elif (GPIO.digitalRead(PUSH_SW_TYOKI) == GPIO.HIGH):
            man = 2
        elif (GPIO.digitalRead(PUSH_SW_PAA) == GPIO.HIGH):
            man = 3

    GPIO.digitalWrite( LED_JYAN, GPIO.LOW)
    GPIO.digitalWrite( LED_AIKO, GPIO.LOW)
    #print(man)                                                  #デバッグ用 1/29 21:00デバッグテストおｋ


    #-----   CPU乱数入力   -----


    cpu = (random.randint(1,100) % 3) + 1


    #-----   互いの手札LED出力   -----


    if man == 1:
        GPIO.digitalWrite( LED_M_GUU, GPIO.HIGH)
    elif man == 2:
        GPIO.digitalWrite( LED_M_TYOKI, GPIO.HIGH)
    else:
        GPIO.digitalWrite( LED_M_PAA, GPIO.HIGH)

    if cpu == 1:
        GPIO.digitalWrite( LED_C_GUU, GPIO.HIGH)
    elif cpu == 2:
        GPIO.digitalWrite( LED_C_TYOKI, GPIO.HIGH)
    else:
        GPIO.digitalWrite( LED_C_PAA, GPIO.HIGH)
    time.sleep(1)


    #-----   じゃんけん処理   -----


    if man == cpu:
        aiko =1
        continue

    elif ((man == 1 and cpu == 2)
        or(man == 2 and cpu == 3)
        or(man == 3 and cpu == 1)):
        win += 1

    else:
        lose += 1

#    print(win)                                                 #デバッグ用 1/29 24：00デバッグテストおｋ
#    print(lose)


    #-----   トータル勝敗処理   -----


    if win == 1:
        GPIO.digitalWrite( LED_M_WIN_1, GPIO.HIGH)

    elif win == 2:
        GPIO.digitalWrite( LED_M_WIN_2, GPIO.HIGH)

    elif win == 3:
        GPIO.digitalWrite( LED_M_WIN_3, GPIO.HIGH)
        time.sleep(1)
        for lp03 in range(2):
            GPIO.digitalWrite( LED_M_WIN_1, GPIO.LOW)
            GPIO.digitalWrite( LED_M_WIN_2, GPIO.LOW)
            GPIO.digitalWrite( LED_M_WIN_3, GPIO.LOW)
            time.sleep(0.5)
            GPIO.digitalWrite( LED_M_WIN_1, GPIO.HIGH)
            GPIO.digitalWrite( LED_M_WIN_2, GPIO.HIGH)
            GPIO.digitalWrite( LED_M_WIN_3, GPIO.HIGH)
            time.sleep(1)
            GPIO.digitalWrite( LED_C_WIN_1, GPIO.LOW)
            GPIO.digitalWrite( LED_C_WIN_2, GPIO.LOW)
            GPIO.digitalWrite( LED_C_WIN_3, GPIO.LOW)
            GPIO.digitalWrite( LED_M_WIN_1, GPIO.LOW)
            GPIO.digitalWrite( LED_M_WIN_2, GPIO.LOW)
            GPIO.digitalWrite( LED_M_WIN_3, GPIO.LOW)
            win = 0
            lose = 0
            continue

    if lose == 1:
        GPIO.digitalWrite( LED_C_WIN_1, GPIO.HIGH)

    elif lose == 2:
        GPIO.digitalWrite( LED_C_WIN_2, GPIO.HIGH)

    elif lose == 3:
        GPIO.digitalWrite( LED_C_WIN_3, GPIO.HIGH)
        time.sleep(1)
        for lp04 in range(2):
            GPIO.digitalWrite( LED_C_WIN_1, GPIO.LOW)
            GPIO.digitalWrite( LED_C_WIN_2, GPIO.LOW)
            GPIO.digitalWrite( LED_C_WIN_3, GPIO.LOW)
            time.sleep(0.5)
            GPIO.digitalWrite( LED_C_WIN_1, GPIO.HIGH)
            GPIO.digitalWrite( LED_C_WIN_2, GPIO.HIGH)
            GPIO.digitalWrite( LED_C_WIN_3, GPIO.HIGH)
            time.sleep(1)
            GPIO.digitalWrite( LED_C_WIN_1, GPIO.LOW)
            GPIO.digitalWrite( LED_C_WIN_2, GPIO.LOW)
            GPIO.digitalWrite( LED_C_WIN_3, GPIO.LOW)
            GPIO.digitalWrite( LED_M_WIN_1, GPIO.LOW)
            GPIO.digitalWrite( LED_M_WIN_2, GPIO.LOW)
            GPIO.digitalWrite( LED_M_WIN_3, GPIO.LOW)
            win = 0
            lose = 0
            continue

    continue
