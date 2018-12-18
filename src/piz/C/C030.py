#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/11 14:01'

# 入力
pixel_list = []
date_list = []
t_list = []

try:
    with open("C030", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt)
        inp_txt.close()
    pixel_list = [int(i) for i in t_list.pop(0).split()]
    for l in t_list:
        n_list = [int(i) for i in l.split()]
        date_list.append(n_list)

except FileNotFoundError:
    pixel_list = [int(i) for i in input().split()]
    for i in range(pixel_list[0]):
        n_list = [int(j) for j in input().split()]
        date_list.append(n_list)

# print("縦: 横 {}".format(pixel_list))
# print("段毎の色素数 {}".format(date_list))

# 処理
for l in date_list:
    change_list = []
    for i in l:
        if i <= 127:
            change_list.append("0")
        else:
            change_list.append("1")
    print(" ".join(change_list))
