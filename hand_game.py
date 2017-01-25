# -*- coding: utf-8 -*-
import time , random

win = 0　　　　　　　　　　　#1
lose = 0
restart = 0

while True:

    if restart == 0:
        print(u"じゃんけんぽん")
    else:
        print(u"あいこでしょ")
        restart = 0

    man = 0
    man = input(u"グー:１　チョキ:２　パー:３")

    cpu = 0
    cpu = random.randint(1,3)
    if cpu ==1:                                    #CPU　グー
        if man == "1":                               #man  グーであいこ
            restart =1
            print(u"cpu グー あいこ")
            continue

        if man == "2":
            lose = lose + 1
            print(u"cpu グー ずこー")            #man チョキで負け
            if lose < 3:
                print(u"勝ち" + str(win) +  "負け" + str(lose))
                time.sleep(1)
                continue
            else:
                print("負けちゃった。もう一回")
                win = 0
                lose = 0
                continue

        if man == "3":                               #man パーで勝ち
            win = win + 1
            print(u"cpu グー やったね")
            if win <3:
                print(u"勝ち" + str(win) + "負け" + str(lose))
                time.sleep(1)
                continue
            else:
                print("おめでとう。もう一回")
                win = 0
                lose = 0
                continue

    if cpu == 2:                                   #cpu チョキ
        if man == "1":                               #man グーで勝ち
            win = win + 1
            print(u"cpu チョキ やったね")
            if win <3:
                print(u"勝ち" + str(win) +  "負け" + str(lose))
                time.sleep(1)
                continue
            else:
                print("おめでとう。もう一回")
                win = 0
                lose = 0
                continue

        if man == "2":                               #man チョキであいこ
            restart =1
            print(u"cpu チョキ あいこ")
            continue

        if man == "3":                               #man パーで負け
            lose = lose + 1
            print(u"cpu チョキ ずこー")
            if lose < 3:
                print(u"勝ち" + str(win) +  "負け" + str(lose))
                time.sleep(1)
                continue
            else:
                print("負けちゃった。もう一回")
                win = 0
                lose = 0
                continue

    if cpu == 3:                                   #cpu パー
        if man == "1":                               #man グーで負け
            lose = lose + 1
            print(u"cpu パー ずこー")
            if lose < 3:
                print(u"勝ち" + str(win) + "負け" + str(lose))
                time.sleep(1)
                continue
            else:
                print("負けちゃった。もう一回")
                win = 0
                lose = 0
                continue

        if man == "2":                               #man チョキで勝ち
            win = win + 1
            print(u"cpu パー やったね")
            if win <3:
                print(u"勝ち" + str(win) + "負け" + str(lose))
                time.sleep(1)
                continue
            else:
                print("おめでとう。もう一回")
                win = 0
                lose = 0
                continue

        if man == "3":                               #man パーであいこ
            restart =1
            print(u"cpu パー あいこ")
            continue
