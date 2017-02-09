# -*- coding: utf-8 -*-

import wiringpi as GPIO
import time
import random

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


order = []
GPIO.digitalWrite( LED_1, GPIO.LOW)
GPIO.digitalWrite( LED_2, GPIO.LOW)
GPIO.digitalWrite( LED_3, GPIO.LOW)
GPIO.digitalWrite( LED_4, GPIO.LOW)
GPIO.digitalWrite( LED_5, GPIO.LOW)
GPIO.digitalWrite( LED_OK, GPIO.LOW)
GPIO.digitalWrite( LED_NG, GPIO.LOW)
slep = float(1)

    #*****スタート入力待ち*****

while slep > 0:
    GPIO.digitalWrite( LED_OK, GPIO.HIGH)
    print(u'スタートボタンを押してください')
    while True:
        if (GPIO.digitalRead(SW_ST) == GPIO.HIGH):
            GPIO.digitalWrite( LED_OK, GPIO.LOW)
            break


    #*****乱数の入力*****


    for lp1 in range(5):
        num = (random.randint(1,100) % 5) + 1
        order.append(num)

    q_no = (random.randint(1,100) % 5)


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
    slep -= 0.1
print(u'おめでとう')