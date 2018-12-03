#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/02 19:11'

import numpy as np

const_date = []
wood_count = 0
wood_p_list = []
t_list = []

try:
    with open("C010", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt)
        inp_txt.close()
        const_date = [int(i) for i in t_list.pop(0).split()]
        wood_count = int(t_list.pop(0))
        for s in t_list:
            n_list = [int(i) for i in s.split()]
            wood_p_list.append(n_list)

except FileNotFoundError:
    const_date = [int(i) for i in input().split()]
    wood_count = int(input())
    for i in range(wood_count):
        n_list = [int(j) for j in input().split()]
        wood_p_list.append(n_list)

# print("工事のx座標: {} 工事のy座標: {} 騒音の大きさ{}".format(const_date[0], const_date[1], const_date[2]))
# print("木陰の場所の数: {}".format(wood_count))
# print("木陰の座標リスト: {}".format(wood_p_list))

# 処理
np_const = np.array(const_date)
for l in wood_p_list:
    l.append(0)
    np_wood_list = np.array(l)
    cal_list = (np_wood_list - np_const) ** 2
    # print(cal_list)
    print("silent" if cal_list[0] + cal_list[1] >= cal_list[2] else "noisy")