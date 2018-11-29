#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/29 11:35'

n_list = []
try:
    with open("D056", "r", encoding="UTF-8") as inp_txt:
        for i in inp_txt:
            n_list = [int(n) for n in i.split()]
        inp_txt.close()

except FileNotFoundError:
    n_list = [int(i) for i in input().split()]

# print(n_list)

# 処理
print((n_list[0] ** 3) - (n_list[1] ** 3))