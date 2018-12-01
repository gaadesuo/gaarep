#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/01 18:16'

# 入力
n = 0
try:
    with open("D074", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            n = int(txt)
        inp_txt.close()

except FileNotFoundError:
    n = int(input())

# print(n)

# 処理
print(n % 24)