# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017//00 :18:07$'


"""
一行目に人数Mと開催数Nが半角スペース区切り与えられる
二行目以下開催の個人の売り上げ予定eが半角スペース区切りで入力される
NもしくはMは0のときがある
この時売り上げ予定から儲けを出せる開催を選び最大でいくら儲けられるかを算出する
0 ≦ N ≦ 1000
0 ≦ M ≦ 1000
-100 ≦ e ≦ 100
"""
inp_num_list = [int(num) for num in input().split()]

# 人数0もしくは開催が0の時は0を出力
if inp_num_list[0] == 0 or inp_num_list[1] == 0:
    print(0)
else:
    buy_date_list = []
    for lp0 in range(inp_num_list[1]):
        inp_date = [int(date) for date in input().split()]
        buy_date_list.append(sum(inp_date))
    # print("開催毎の儲けの合計値" + str(buy_date_list))
    ans_num = 0
    for pricee in buy_date_list:
        # マイナス計上は開催しない
        if pricee >= 0:
            ans_num += pricee

    print("{:0d}".format(ans_num))