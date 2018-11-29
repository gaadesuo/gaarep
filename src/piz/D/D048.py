#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/29 09:23'

# 入力
n_list = []
try:
    with open("D048", "r", encoding="UTF-8") as inp_txt:
        n_list = [int(i.strip()) for i in inp_txt]
        inp_txt.close()

except FileNotFoundError:
    n_list = [int(input()) for i in range(5)]

# print(n_list)

# 処理
for i in range(4):
    print(n_list[i + 1] - n_list[i])