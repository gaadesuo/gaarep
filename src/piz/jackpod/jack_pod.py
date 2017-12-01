# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2017 / 11 / 30

"""
カードの点数
    数字のカード（2～10）は数字どおりの点数です。 
    A（1）は1点または11点、J,Q,K（11,12,13）は10点として計算します。 
    なお、Aはカードの合計値が22点以上にならない限りは11点として扱います。 

バースト
    カードの合計点数が21点をオーバー（22点以上）してしまうと
    その時点でゲームオーバー・相手の勝利となります。 

HIT
    カードを追加で1枚引きます。

STAND
    カードを追加せず、手持ちのカードのみで勝負します。

ディーラーの行動
    ディーラーは基本的に手持ちカードの合計が17以上の場合はSTAND（勝負）し
    17未満の場合はHIT（カードを引く）しますが、ディーラーによっては
    上記以外の行動を取る場合があります。 

連続勝負
    選択する相手ディーラーによって、1回のコード提出で勝負する回数が異なります。
    ディーラー選択画面の「連続勝負」欄を参照してください。

入出力の詳細
    カードを引くか(HIT)、引かないか(STAND)の出力。 
    BET金額を出力する場合以外は、カードを引く場合は'HIT'を
    カードを引かない場合は、'STAND'を出力してください。 
"""

# 全カードのリスト作成
card_num = []
for num in range(1, 14):
    for lp0 in range(4):
        card_num.append(num)

total = 0
# 1ループ目はチップ情報が与えられる。my_card[0]の値は0なのでチップを掛ける
my_card = [int(num) for num in input().split()]
flag = 0

if my_card[0] == 0:
    # 掛けるチップの枚数
    print("1")

else:
    """
    自分のポイントの確認
    """
    # 最初に今まで引いたカードの数字を引く
    for num in my_card:
        card_num.remove(num)
    for num in my_card:
        # 1の時は一の枚数文フラグをたてる
        if num == 1:
            flag += 1
            total += 11
        # 10以上の時
        elif num == 11 or num == 12 or num == 13:
            total += 10
        else:
            total += num
    # print("自分のポイントは: {:0d}".format(total))

    """
    カードを引くか引かないかの判定
    """
    # 1があるかの確認
    if flag > 0:
        if total > 21:
            # 1の枚数を1にして計算する
            for ace in range(flag):
                total -= 10 * (ace + 1)
                if total > 21:
                    pass
                # 1を1の計算で18～21ならSTANDするため抜ける
                elif 18 <= total <= 21:
                    break

    # 18以下ならカードを引く
    if total <= 17:
        print("HIT")
    else:
        print("STAND")
