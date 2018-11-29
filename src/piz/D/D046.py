#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/29 08:44'

# 入力
n_list =[]
try:
    with open("D046", "r", encoding="UTF-8") as inp_txt:
        for i in inp_txt:
            n_list = [int(n) for n in i.strip().split()]
        inp_txt.close()

except FileNotFoundError:
    n_list = [int(n) for n in input().split()]

# 処理
print(max(n_list))