#! /usr/bin/python
# -*-coding: utf-8-*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "user"
__date__ = "$2017/02/26 1:32:29$"


import wiringpi as GPIO


#-----GPIO初期設定-----


LED_RED     = 16      #右18
LED_GREEN   = 20      #右19
LED_BULE    = 21      #右20

SW_RED_UP   = 13      #左17
SW_GREEN_UP = 19      #左18
SW_BULE_UP  = 26      #左19

SW_RED_DN   = 17      #左06
SW_GREEN_DN = 27      #左07
SW_BULE_DN  = 22      #左08

SW_END      = 12      #右16


GPIO.wiringPiSetupGpio()

GPIO.pinMode(LED_RED,GPIO.OUTPUT)
GPIO.pinMode(LED_GREEN,GPIO.OUTPUT)
GPIO.pinMode(LED_BULE,GPIO.OUTPUT)

#以下入力注意
GPIO.pinMode(SW_RED_UP,GPIO.INPUT)
GPIO.pinMode(SW_GREEN_UP,GPIO.INPUT)
GPIO.pinMode(SW_BULE_UP,GPIO.INPUT)
GPIO.pinMode(SW_RED_DN,GPIO.INPUT)
GPIO.pinMode(SW_GREEN_DN,GPIO.INPUT)
GPIO.pinMode(SW_BULE_DN,GPIO.INPUT)
GPIO.pinMode(SW_END,GPIO.INPUT)

#以下PWMの設定
GPIO.softPwmCreate(LED_RED,0,100)
GPIO.softPwmCreate(LED_GREEN,0,100)
GPIO.softPwmCreate(LED_BULE,0,100)

#以下プルダウンの設定
GPIO.pullUpDnControl(SW_RED_UP,GPIO.PUD_DOWN)
GPIO.pullUpDnControl(SW_GREEN_UP,GPIO.PUD_DOWN)
GPIO.pullUpDnControl(SW_BULE_UP,GPIO.PUD_DOWN)
GPIO.pullUpDnControl(SW_RED_DN,GPIO.PUD_DOWN)
GPIO.pullUpDnControl(SW_GREEN_DN,GPIO.PUD_DOWN)
GPIO.pullUpDnControl(SW_BULE_DN,GPIO.PUD_DOWN)
GPIO.pullUpDnControl(SW_END,GPIO.PUD_DOWN)

#初期値
PWM_R = 0
PWM_G = 0
PWM_B = 0


if __name__ == "__main__":


    #-----PWMの値決定-----


    while (GPIO.digitalRead(SW_END) == GPIO.LOW):
        if (GPIO.digitalRead(SW_RED_UP) == GPIO.HIGH):
            PWM_R += 10
            print('R' + str(PWM_R) + 'G' + str(PWM_G) + 'B' + str(PWM_B))
        elif (GPIO.digitalRead(SW_GREEN_UP) == GPIO.HIGH):
            PWM_G += 10
            print('R' + str(PWM_R) + 'G' + str(PWM_G) + 'B' + str(PWM_B))
        elif (GPIO.digitalRead(SW_BULE_UP) == GPIO.HIGH):
            PWM_B += 10
            print('R' + str(PWM_R) + 'G' + str(PWM_G) + 'B' + str(PWM_B))
        elif (GPIO.digitalRead(SW_RED_DN) == GPIO.HIGH):
            PWM_R -= 10
            print('R' + str(PWM_R) + 'G' + str(PWM_G) + 'B' + str(PWM_B))
        elif (GPIO.digitalRead(SW_GREEN_DN) == GPIO.HIGH):
            PWM_G -= 10
            print('R' + str(PWM_R) + 'G' + str(PWM_G) + 'B' + str(PWM_B))
        elif (GPIO.digitalRead(SW_BULE_DN) == GPIO.HIGH):
            PWM_B -= 10
            print('R' + str(PWM_R) + 'G' + str(PWM_G) + 'B' + str(PWM_B))

        #0以下もしくは100以上のときは0もしくは100にする
        if PWM_R < 0:
            PWM_R = 0
        if PWM_R > 100:
            PWM_R = 100
        if PWM_G < 0:
            PWM_G = 0
        if PWM_G > 100:
            PWM_G = 100
        if PWM_B < 0:
            PWM_B = 0
        if PWM_B > 100:
            PWM_B = 100

        while ((GPIO.digitalRead(SW_RED_UP) == GPIO.HIGH)
        or (GPIO.digitalRead(SW_RED_DN) == GPIO.HIGH)
        or (GPIO.digitalRead(SW_GREEN_UP) == GPIO.HIGH)
        or (GPIO.digitalRead(SW_GREEN_DN) == GPIO.HIGH)
        or (GPIO.digitalRead(SW_BULE_UP) == GPIO.HIGH)
        or (GPIO.digitalRead(SW_BULE_DN) == GPIO.HIGH)):
            continue



        #-----LEDのPWM制御-----


        GPIO.softPwmWrite(LED_RED,PWM_R)
        GPIO.softPwmWrite(LED_GREEN,PWM_G)
        GPIO.softPwmWrite(LED_BULE,PWM_B)


    #-----終了処理-----


    GPIO.softPwmWrite(LED_RED,0)
    GPIO.softPwmWrite(LED_GREEN,0)
    GPIO.softPwmWrite(LED_BULE,0)
