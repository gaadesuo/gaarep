# -*- coding: utf-8 -*-
import random,time,sys

print(u"""------------------------------------
           ジャンケンゲーム
------------------------------------""")


while True:



    #---初期化---
    win = 0
    lose = 0



    print(u"""
*** じゃんけんぽん ***
""")                    

    while True:



        #---人間入力---
        print(u"""何を出す？
1: グー    2: チョキ    3: パー
""")
        man = input(">>> ")



        #---cpu入力乱数の偏り修正版---
        cpu = (random.randint(1,100) % 3) + 1



        #---お互いの手の内表示処理---
        if man == "1":
            man = int(1)
            munhd = "グー"
        elif man == "2":
            man = int(2)
            munhd = "チョキ"
        elif man == "3":
            man = int(3)
            munhd = "パー"
        else:
            print(u"そんな形の出し手ないよ！もう一回、じゃんけんぽん！")
            continue

        if cpu == 1:
            cpuhd = "グー"
        elif cpu ==2:
            cpuhd = "チョキ"
        else:
            cpuhd = " パー"

        print(u"あなた: " + str(munhd) + "    コンピューター: " + str(cpuhd))



        #---勝敗処理---
        if man == cpu:
            print(u"""
*** あいこでしょ！ ***
            """)
            continue

        elif((man == 1 and cpu == 2)
           or(man == 2 and cpu == 3)
           or(man == 3 and cpu == 1)):
            print(u"""
*** やったね ! ***
            """)
            win += 1

        else:
            print("""
*** ずこー ***
            """)
            lose += 1


        #---結果表示---
        if win == 3:
            print("""
*** おめでとう ！***
            """)
            break

        elif lose == 3:
            print("""
*** 残念だったね！ ***
            """)
            break

        else:
            print("""
*** あなた: """ + str (win) + "勝    コンピューター: " + str(lose) + """勝 ***
""")
            continue
    print(u"""*** もう一度やる？ ***
はい: 1    いいえ: 2""")
    onemore = input(">>> ")
    if onemore == "1":
        continue
    elif onemore  == "2":
        print(u"*** またやろうね ***")
        sys.exit()
    else :
        print(u"""*** 死ねばいいと思うよ ***
そう言って相手は去って行った""")
        sys.exit()

