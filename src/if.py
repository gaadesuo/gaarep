# -*- coding utf-8 -*-

#ラズパイで電子工作（スイッチを使ったLチカ用source

TOGGLE_SW = 14        #PIN番号8
PUSH_SW_ON = 15       #PIN番号10
PUSH_SW_OFF = 18      #PIN番号12
LED_1 = 23            #PIN番号16
LED_2 = 24            #PIN番号18

GPIO.wiringPiSetupGpio()
GPIO.pinMode( TOGGLE_SW, GPIO.INPUT )        #入力設定※注意
GPIO.pinMode( PUSH_SW_ON, GPIO.INPUT )       #入力設定※注意
GPIO.pinMode( PUSH_SW_OFF, GPIO.INPUT )      #入力設定※注意
GPIO.pinMode( LED_1, GPIO.OUTPUT )           #出力設定
GPIO.pinMode( LED_2, GPIO.OUTPUT )           #出力設定

"""-----------------------------------------------------------------------------------***

                                     変数

***-----------------------------------------------------------------------------------"""

a = 0        #メインスイッチのフラグ用変数
b = 0        #ON用フラグ変数（押しボタン、画面操作兼用
c = 0        #OFFボタンフラグ用変数

"""-----------------------------------------------------------------------------------***

                                   実行部分

***-----------------------------------------------------------------------------------"""

print (u"メインスイッチが入っていません")
print(u"メインスイッチが入るまで待機します。プログラムを終了する場合はCTRL+Zを押してください")
while True:        #メインスイッチの確認ループ

#---- メインスイッチが入るまで確認ループ ----

    if ( GPIO.digitalRead( TOGGLE_SW ) == GPIO.HIGH ):        #メインスイッチが入ってるかの確認 ※入力注意
        a = 1
        print (u"電源が入りました。ONスイッチを押すと点滅を開始します。")
        while a == 1:        #メインスイッチが入ってる間はループ

        #---- メインスイッチが入って点滅押されるまでこの間をループ ----
            if ( GPIO.digitalRead( TOGGLE_SW ) == GPIO.LOW ):        #メインスイッチが入ってるかの確認 ※入力注意
                a = 0
            if ( GPIO.digitalRead( PUSH_SW_ON ) == GPIO.HIGH ):        #※入力注意
                b = 1
                if b == 1:
                    print (u"点滅中です。")
                    while a == 1:        #メインスイッチが入ってる間はループ
                        
                        #---- OFF信号が出力されるまでループ ----
                        if ( GPIO.digitalRead( TOGGLE_SW ) == GPIO.LOW ):        #メインスイッチが入ってるかの確認 ※入力注意
                            a = 0
                        if ( GPIO.digitalRead( PUSH_SW_OFF ) == GPIO.HIGH ):        #※入力注意！
                            c = 1
                            b = 0
                            if c == 1:
                                print (u"LEDが消灯しました。ONスイッチを押してください")
                                c = 0
                                break        #消灯信号でループを抜ける
                        else:        #OFF信号がない時はLED点灯

                            #----****    ここからLED点滅のsource    ****----
                            
                            GPIO.digitalWrite( LED_1, GPIO.HIGH )
                            time.sleep( 0.5 )
                            GPIO.digitalWrite( LED_1, GPIO.LOW )
                            GPIO.digitalWrite( LED_2, GPIO.HIGH )
                            time.sleep( 0.5 )
                            GPIO.digitalWrite( LED_2, GPIO.LOW )
                            
                            #----****    ここまでLED点滅のsource    ****----

                        #---- OFF信号出力されるまでここまでループ ----
                        
                    else:
                        print (u"メインスイッチが切られました。メインスイッチが入るまで待機します。プログラムを終了する場合はCTRL+Zを押してく>ださい")
                        break
            else:
                print (u"メインスイッチが切られました。メインスイッチが入るまで待機します。プログラムを終了する場合はCTRL+Zを押してください")
#            break
            #---- メインスイッチが切れるか点滅が押されるまでループここまで ----
#---- メインスイッチの確認ループここまで ----
