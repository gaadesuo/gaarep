#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/05 09:02'

import numpy as np

# 入力
hit_list = []
lottery_list = []
t_list = []

try:
    with open("C023", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt)
        inp_txt.close()
    hit_list = [int(i) for i in t_list.pop(0).split()]
    for l in t_list[1:]:
        n_list = [int(i) for i in l.split()]
        lottery_list.append(n_list)

except FileNotFoundError:
    hit_list = [int(i) for i in input().split()]
    for i in range(int(input())):
        n_list = [int(i) for i in input().split()]
        lottery_list.append(n_list)

# print("当選番号: {}".format(hit_list))
# print("クジの番号: {}".format(lottery_list))

# 処理
hit_num = 0
for l in lottery_list:
    np_lott = np.array(l)
    for i in hit_list:
        # print(i, np_lott)
        if np.any(np_lott == i):
            hit_num += 1
    print(hit_num)
    hit_num = 0
