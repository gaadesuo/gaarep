# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "user"
__date__ = "$2017/02/23 12:46:08$"

import wiringpi as GPIO
import time


#-----GPIOの初期設定----


OUT = 26       #左側19

GPIO.wiringPiSetupGpio()
GPIO.pinMode(OUT,GPIO.OUTPUT)


#-----実行部分-----


if __name__ == "__main__":


    #-----発信信号の時間の辞書
    #キーは文字で値は長さ
    dic ={
    's':[2,2,2],
    'o':[1,1,1]}


    #-----入力-----


    while True:
        str = input(u'発信したい文字を半角英数、ひらがなで入れてください >> ')
        strlist = list(str)
        stccount = len(strlist)

        #strlistの中身を一つづつ文字の検索して一致してればokをcountの中に入れる
        #すべてを検索し終えた後にstrlistとcountの要素数が同じなら前一致なのでループを抜ける
        count = ['ok' for match in strlist
            if (u'ぁ' <= match <= u'ん'
            or   'A'  <= match <= 'Z'
            or   'a'  <= match <= 'z'
            or   '1'  <= match <= '9')]
        if len(count) == len(strlist):
            break
        else:
            print(u'入力された文字が不適切です。もう一度入力してください')
            continue


    #-----発信信号作成-----


    for word in strlist:
        sign = dic[word]
        #デバッグ用
        #print(sign)
        for long in sign:
            #デバッグ用
            #print(long)
            GPIO.digitalWrite(OUT,GPIO.HIGH)
            time.sleep(long / 5)
            GPIO.digitalWrite(OUT,GPIO.LOW)
            time.sleep(0.1)