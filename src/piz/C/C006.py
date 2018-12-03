#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/02 17:42'

import numpy as np

# 入力
date_list = []
mag_list = []
point_list = []
t_list = []

try:
    with open("C006", "r", encoding="UTF-8")as inp_txt:
        for txt in inp_txt:
            t_list.append(txt)
        inp_txt.close()
        date_list = [int(i) for i in t_list.pop(0).split()]
        mag_list = [float(i) for i in t_list.pop(0).split()]
        for i in t_list:
            j_list = [int(j) for j in i.split()]
            point_list.append(j_list)

except FileNotFoundError:
    date_list = [int(i) for i in input().split()]
    mag_list = [float(i) for i in input().split()]
    for i in range(date_list[1]):
        temp_point = [int(i) for i in input().split()]
        point_list.append(temp_point)

# print("パラメータの数: {} 人数: {} 表示する上位: {}".format(date_list[0], date_list[1], date_list[2]))
# print("倍率: {}".format(mag_list))
# print("ポイントリスト: {}".format(point_list))

# 処理
total_p_list = []

# 四捨五入用関数
n_round = lambda x: (x * 2 + 1) // 2

np_mag = np.array(mag_list)
for l in point_list:
    np_point = np.array(l)
    temp_point = (np_mag * np_point)
    # print("倍率を掛けた後のポイント: {}".format(temp_point))

    # 合計したものを四捨五入し整数化
    ans = int(n_round(sum(temp_point)))
    # print(ans)
    total_p_list.append(ans)


sort_list = sorted(total_p_list, reverse=True)
# print(sort_list)
for i in range(date_list[2]):
    print(sort_list[i])