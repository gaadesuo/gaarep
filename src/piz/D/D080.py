#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/01 19:41'

# 入力
n_list = []
try:
    with open("D080", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            n_list = [int(i) for i in txt.split()]
        inp_txt.close()

except FileNotFoundError:
    n_list = [int(i) for i in input().split()]

# print(n_list)

# 処理
print((n_list[0] * 6000) + (n_list[1] * 4000))