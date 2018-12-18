#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/05 08:47'

# 入力
date_num = []
grid_list = []
t_list = []

try:
    with open("C021", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt)
        inp_txt.close()
        date_num =[int(i) for i in t_list.pop(0).split()]
        for l in t_list[1:]:
            n_list = [int(i) for i in l.split()]
            grid_list.append(n_list)

except FileNotFoundError:
    date_num =[int(i) for i in input().split()]
    for i in range(int(input())):
        n_list = [int(i) for i in input().split()]
        grid_list.append(n_list)

# print("中心座標x, y, 内周円の大きさ, 外周円の大きさ {}".format(date_num))
# print("座標リスト: {}".format(grid_list))

# 処理
for l in grid_list:
    grid_math = ((l[0]- date_num[0]) ** 2) + ((l[1] - date_num[1]) ** 2)
    # print(grid_math)
    if date_num[2] ** 2 <= grid_math <= date_num[3] ** 2:
        print("yes")
    else:
        print("no")