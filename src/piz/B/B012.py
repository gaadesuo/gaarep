# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2017 / 11 / 25

inp_date_list = []
for lp0 in range(int(input())):
    inp_date = input()
    # 最後の数値を抜いて数値化してリストに入れる
    date_list = [int(num) for num in inp_date[:15]]
    inp_date_list.append(date_list)

even_num = 0
odd_num = 0
for date in inp_date_list:
    # 奇数桁の合計を求める
    for even in range(1, 14, 2):
        even_num += date[even]
    # 偶数桁の2倍(注)合計を求める (注)2倍したとき2桁なら桁同士を足し1桁にする
    for odd in range(0, 15, 2):
        # 2倍したものが二けたなら桁同士を足して一けたにする
        odd_2 = date[odd] * 2
        if odd_2 >= 10:
            odd_2 = int(odd_2 / 10) + (odd_2 % 10)
        odd_num += odd_2
    # print("偶数の2倍の合計は:{} 奇数の合計は:{}".format(odd_num,even_num))
    total_num = odd_num + even_num
    # print("合計は:{:0d}".format(total_num))
    # 10から1桁目を引いて10の倍数になるようにする。0の時は0のまま
    ans_num = 0 if total_num % 10 == 0 else 10 - (total_num % 10)
    print("{:0d}".format(ans_num))
    odd_num = 0
    even_num = 0



