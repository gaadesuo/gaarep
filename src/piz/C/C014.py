#! python3
# -*- coding: utf-8 -*-

__author__ = "gaa"
__date__ = '2018/12/03 20:00'

# 入力
date_list = []
box_list = []
t_list = []
try:
    with open("C014", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt)
        inp_txt.close()
        date_list = [int(i) for i in t_list.pop(0).split()]
        for i in t_list:
            n_list = [int(j) for j in i.split()]
            box_list.append(n_list)

except FileNotFoundError:
    date_list = [int(i) for i in input().split()]
    for i in range(date_list[0]):
        n_list = [int(j) for j in input().split()]
        box_list.append(n_list)

# print("箱の数: {} 球の半径: {}".format(date_list[0], date_list[1]))
# print("箱の各長さのリスト: {}".format(ball_list))

# 処理
min_num_list = []
ans_list = []

for l in box_list:
    min_num_list.append(min(l))
ans_list = [i + 1 for i in range(date_list[0]) if min_num_list[i] >= date_list[1] * 2]
# print(ans_list)

for i in ans_list:
    print(i)

