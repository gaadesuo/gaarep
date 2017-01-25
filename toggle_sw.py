# -*- coding: utf-8 -*-

#mixi日記スイッチ回路実践のsource

import wiringpi as GPIO , time

#トグルスイッチGPIO番号
TOGGLE_SW = 15

GPIO.wiringPiSetupGpio()
#（注）入力モード
GPIO.pinMode( TOGGLE_SW, GPIO.INPUT )

print (u"(´・ω・｀)ここは僕たちのスレだよ。きうり食べる？")
while True:
        if ( GPIO.digitalRead( TOGGLE_SW ) == GPIO.HIGH ):
            print ("彡(ﾟ)(ﾟ)なんやて！")
            break
        else:
            time.sleep( 0.1 )
