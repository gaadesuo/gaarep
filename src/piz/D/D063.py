#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/30 08:55'

import numpy as np

t_list = []
n_list = []
n = 0
try:
    with open("D063", "r", encoding="UTF-8") as inp_txt:
        for i in inp_txt:
            t_list.append(i.strip())
        inp_txt.close()
        # print(t_list)
        n_list = [int(n) for n in t_list[0].split()]
        n = int(t_list[1])

except FileNotFoundError:
    n_list = [int(n) for n in input().split()]
    n = int(input())

# print(n, n_list)

# 処理
np_list = np.array(n_list)
position = np.where(np_list >= n)
print((len(np_list) + 1) if len(position[0]) == 0 else min(position[0]) + 1)