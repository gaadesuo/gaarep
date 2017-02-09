# -*- coding: utf-8 -*-

__author__ = "user"
__date__ = "$2017/02/08 16:58:47$"

if __name__ == "__main__":

    import wiringpi as GPIO
    import time
    import random


    #*****GPIOPINの設定*****

    LED_1 = 5        #左15
    LED_2 = 6        #左16
    LED_3 = 13       #左17
    LED_4 = 19       #左18
    LED_5 = 26       #左19
    LED_OK = 23      #右8
    LED_NG = 24      #右9

    SW_1 = 8         #右12
    SW_2 = 7         #右13
    SW_3 = 16        #右18
    SW_4 = 20        #右19
    SW_5 = 21        #右20
    SW_ST = 12       #右16


    GPIO.wiringPiSetupGpio()

    GPIO.pinMode( LED_1, GPIO.OUTPUT)
    GPIO.pinMode( LED_2, GPIO.OUTPUT)
    GPIO.pinMode( LED_3, GPIO.OUTPUT)
    GPIO.pinMode( LED_4, GPIO.OUTPUT)
    GPIO.pinMode( LED_5, GPIO.OUTPUT)
    GPIO.pinMode( LED_OK, GPIO.OUTPUT)
    GPIO.pinMode( LED_NG, GPIO.OUTPUT)

    #以下入力注意
    GPIO.pinMode( SW_1,GPIO.INPUT)
    GPIO.pinMode( SW_2,GPIO.INPUT)
    GPIO.pinMode( SW_3,GPIO.INPUT)
    GPIO.pinMode( SW_4,GPIO.INPUT)
    GPIO.pinMode( SW_5,GPIO.INPUT)
    GPIO.pinMode( SW_ST,GPIO.INPUT)


    #*****初期設定*****


    GPIO.digitalWrite( LED_1, GPIO.LOW)
    GPIO.digitalWrite( LED_2, GPIO.LOW)
    GPIO.digitalWrite( LED_3, GPIO.LOW)
    GPIO.digitalWrite( LED_4, GPIO.LOW)
    GPIO.digitalWrite( LED_5, GPIO.LOW)
    GPIO.digitalWrite( LED_OK, GPIO.LOW)
    GPIO.digitalWrite( LED_NG, GPIO.LOW)
    slep = float(1)


    #*****説明出力*****


    print(u'''***********************************************************
スタートボタンを押すとLEDが光るから、順番を覚えてね
その後に画面に問題が出るからそれに答えよう
正解すると緑のLED、間違えると黄色のLEDが光るよ
正解するとどんどんLEDの光るスピードが上がっていくんだ
間違えたら終わりだよ
どこまでいけるかレッツチャレンジ
***********************************************************
''')


    #*****ループ開始とスタート待ち*****


    #0.1秒でゲームクリア
    while slep > 0.1:
        #ゲーム開始でリストを空にする
        order = []
        input_no = []
        print(u'スタートボタンを押してLEDの順番を覚えよう')
        while True:
            if (GPIO.digitalRead(SW_ST) == GPIO.HIGH):
                break


        #*****乱数の入力*****


        for lp1 in range(5):
            led_no = (random.randint(1,100) % 5) + 1
            order.append(led_no)

        que_no = (random.randint(1,100) % 5)


        #*****LED点滅*****


        for ele in range(0,5):
            if order[ele] == 1:
                GPIO.digitalWrite( LED_1, GPIO.HIGH)
                time.sleep(slep)
                GPIO.digitalWrite( LED_1, GPIO.LOW)
                time.sleep(0.1)
            elif order[ele] == 2:
                GPIO.digitalWrite( LED_2, GPIO.HIGH)
                time.sleep(slep)
                GPIO.digitalWrite( LED_2, GPIO.LOW)
                time.sleep(0.1)
            elif order[ele] == 3:
                GPIO.digitalWrite( LED_3, GPIO.HIGH)
                time.sleep(slep)
                GPIO.digitalWrite( LED_3, GPIO.LOW)
                time.sleep(0.1)
            elif order[ele] == 4:
                GPIO.digitalWrite( LED_4, GPIO.HIGH)
                time.sleep(slep)
                GPIO.digitalWrite( LED_4, GPIO.LOW)
                time.sleep(0.1)
            else:
                GPIO.digitalWrite( LED_5, GPIO.HIGH)
                time.sleep(slep)
                GPIO.digitalWrite( LED_5, GPIO.LOW)
                time.sleep(0.1)


        #*****問題出力*****


        if que_no == 0:
            print(u'光った順番にボタンを入力して最後にスタートボタンを押してね')
        else:
            print(str(que_no) + u'番目に光ったLEDのボタンを押してね')


        #*****入力と合否判定*****


        while True:
            if (GPIO.digitalRead(SW_ST) == GPIO.HIGH):
                break
            else:
                if (GPIO.digitalRead(SW_1) == GPIO.HIGH):
                    sw_no = 1
                elif (GPIO.digitalRead(SW_2) == GPIO.HIGH):
                    sw_no = 2
                elif (GPIO.digitalRead(SW_3) == GPIO.HIGH):
                    sw_no = 3
                elif (GPIO.digitalRead(SW_4) == GPIO.HIGH):
                    sw_no = 4
                else:
                    sw_no = 5

                input_no.append(int(sw_no))

        if pue_no == 0:
            if order != input_no:
                break
        else:
            if order[que_no - 1] != sw_no:
                break
            print(u'正解だよ！次も頑張って！')
            slep -= 0.1
    else:
        print(u'ゲームクリア！すごいね！')
    print(u'残念、間違いだよ')
