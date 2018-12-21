#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/18 19:37'

import numpy as np

# 入力
date_list = []
live_list = []
t_list = []

try:
    with open("B008", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list = [int(i) for i in txt.split()]
            live_list.append(t_list)
        inp_txt.close()
    date_list = live_list.pop(0)

except FileNotFoundError:
    date_list = [int(i) for i in input().split()]
    if date_list[0] == 0 or date_list[1] == 0:
        pass
    else:
        for i in range(date_list[1]):
            t_list = [int(j) for j in input().split()]
            live_list.append(t_list)

# print("会員数: 開催数: {}".format(date_list))
# print("開催時の採算リスト{}".format(live_list))

# 処理
if date_list[0] == 0 or date_list[1] == 0:
    print("0")

else:
    np_live_list = np.array(live_list)
    live_sum_list = np.sum(np_live_list, axis=1)
    # print(live_sum_list)
    plus_index = np.where(live_sum_list > 0)
    for i in plus_index:
        print(sum(live_sum_list[i]))


