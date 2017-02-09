# -*-coding:utf-8 -*-

#mixi 日記LEDで並列回路、アイスはすべて解けたのsource

import time,wiringpi as GPIO

#LEDを使用するGPIO番号
LED1 = 14
LED2 = 15

GPIO.wiringPiSetupGpio()

#共に出力
GPIO.pinMode( LED1, GPIO.OUTPUT )
GPIO.pinMode( LED2, GPIO.OUTPUT )

counter = 0


#２回繰り返して終わりを表示して終了
for counter in range(0, 2):

    GPIO.digitalWrite( LED1, GPIO.HIGH )
    time.sleep( 0.5 )
    GPIO.digitalWrite( LED1, GPIO.LOW )
    time.sleep( 0.5 )

    GPIO.digitalWrite( LED2, GPIO.HIGH )
    time.sleep( 0.5 )
    GPIO.digitalWrite( LED2, GPIO.LOW )
    time.sleep( 0.5 )

    GPIO.digitalWrite( LED1, GPIO.HIGH )
    GPIO.digitalWrite( LED2, GPIO.HIGH )
    time.sleep( 1 )

    GPIO.digitalWrite( LED1, GPIO.LOW )
    GPIO.digitalWrite( LED2, GPIO.LOW )
    time.sleep( 1 )

print (u"終わり")
