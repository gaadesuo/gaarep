#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/27 09:52'

# 入力
n_l = []
try:
    with open("D040", "r", encoding="UTF-8") as inp_txt:
        n_l = [int(i.strip()) for i in inp_txt]
        inp_txt.close()

except FileNotFoundError:
    n_l = [int(input()) for i in range(7)]

# print(n_l)

# 処理
print(sum(n <= 30 for n in n_l))