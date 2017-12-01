# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2017 / 11 / 30

import numpy as np

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


def point_check(card_list):
    """
    与えられたカードリストから限りなく有利なポイントを割り出す
    :param card_list: カードの数字群
    :return: 配られたカードの現在のポイント
    """
    global card_num
    flag = 0
    temp_total = 0

    # 与えられたリストの数字を残カードリストから引く
    for num in card_list:
        card_num.remove(num)
    for num in card_list:
        # 1のカードがある場合枚数分カウント
        if num == 1:
            flag += 1
            temp_total += 11
        # カードが10以上の時10にする
        elif num == 11 or num == 12 or num == 13:
            temp_total += 10
        else:
            temp_total += num
    # print("自分のポイントは: {:0d}".format(total))

    # ***1がある時の条件判定***
    if flag > 0:
        if temp_total > 21:
            # 1の枚数を1にして計算する
            for ace in range(flag):
                temp_total -= 10 * (ace + 1)
                if temp_total > 21:
                    pass
                # 1を1の計算で18～21なら抜ける
                elif stand_min <= total <= 21:
                    break
    return temp_total


# ***変数***

# ディーラーの選択
dealer_select = 2
# 0: 猫先生 霧島京子
# 1:緑川つばめ 六村リオ
# 2: 霧島京子(バニー)
total = 0
dealer = 0
# flag = 0
dealer_flag = 0
# チップを掛けるベース, 連勝ごとに数値の倍数を掛けていく
chip = 1
# standの最低数値 これ以上ならSTAND指示
stand_min = 18
round_num = 0
win_num = 0

# ***全カードのリスト作成***

card_num = []
for num in range(1, 14):
    for lp0 in range(4):
        card_num.append(num)

# ***入力***

my_card = list(map(int, input().split()))
# 緑川つばめ以降の入力
if dealer_select >= 1:
    round_num = int(input())
    win_num = int(input())
# 霧島京子(バニー)以降で最初のチップ入力じゃない場合
if dealer_select >= 2 and my_card[0] != 0:
    max_bet = int(input())
    dealer_card = list(map(int, input().split()))


# ***判定***

# インデックス0が0の値の時はチップのベットタイミング
if my_card[0] == 0:
    # 連勝時には基本betに連勝数を掛けてbet
    print(str(chip * (win_num + 1)))

# カード入力
else:
    # 自分のポイント判定
    total = point_check(my_card)

    # ***ディーラーの選択が0か1の場合***
    if dealer_select == 0 or dealer_select == 1:
        if stand_min <= total:
            print("STAND")
        else:
            print("HIT")

    # ***ディーラーの選択が2の場合
    elif dealer_select == 2:
        # デーラーポイント計算
        dealer = point_check(dealer_card)

        # 残りのカードから21になるまでのカードの残りを別リストに入れる
        np_card_num = np.array(card_num)
        remaining_list = np.where(np_card_num <= (21 - total))

        # ディーラーがブラックジャックかドボンの場合はひかない
        if dealer >= 21:
            print("STAND")
        # ディラーより数値が低い場合は無条件で引く
        elif total <= dealer:
            print("HIT")
        # 18～21なら引かない
        elif 18 <= total <= 21:
            print("STAND")
        else:
            # 21までの残りカードが今まで一枚も出ていない場合
            if len(remaining_list) > ((21 - total) * 4):
                print("HIT")
            else:
                print("STAND")
