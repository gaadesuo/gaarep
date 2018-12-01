#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/30 22:15'

# 入力
n_list = []
try:
    with open("D071", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            n_list = [int(n) for n in txt.split()]
        inp_txt.close()

except FileNotFoundError:
    n_list = [int(n) for n in input().split()]

# print(n_list)

# 処理
if n_list[0] >= 25 or n_list[1] <= 40:
    if n_list[0] >= 25 and n_list[1] <= 40:
        print("No")
    else:
        print("Yes")
else:
    print("No")