#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/25 21:22'

# 入力
try:
    with open("D024", "r", encoding="UTF-8") as inp_txt:
        n_0, n_1 = [int(i.strip()) for i in inp_txt]
        inp_txt.close()

except FileNotFoundError:
    n_0 = int(input())
    n_1 = int(input())

# print(n_0, n_1)

# 処理
print(180 - n_0 - n_1)