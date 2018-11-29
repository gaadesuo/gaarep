#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/30 07:45'

# 入力
n_list = []
try:
    with open("D058", "r", encoding="UTF-8") as inp_txt:
        for i in inp_txt:
            n_list = [int(n) for n in i.split()]
        inp_txt.close()

except FileNotFoundError:
    n_list = [int(i) for i in input().split()]

# print(n_list)

# 処理
print("{}{}{}".format("A" * n_list[0], "B" * n_list[1], "A" * n_list[2]))