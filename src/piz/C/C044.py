#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/17 19:54'

import collections

# 入力
hand_list = []

try:
    with open("C044", "r" , encoding="UTF-8") as inp_txt:
        next(inp_txt)
        for txt in inp_txt:
            hand_list.append(txt.strip())
        inp_txt.close()

except FileNotFoundError:
    for i in range(int(input())):
        hand_list.append(input())

# print("じゃんけんの手: {}".format(hand_list))

# 処理
col_hand_dic = collections.Counter(hand_list)
# print(col_hand_dic)
if len(col_hand_dic.keys()) != 2:
    print("draw")

elif ("paper" in col_hand_dic) and ("rock" in col_hand_dic):
    print("paper")

elif ("scissors" in col_hand_dic) and ("paper" in col_hand_dic):
    print("scissors")

elif ("rock" in col_hand_dic) and ("scissors" in col_hand_dic):
    print("rock")