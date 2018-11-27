#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/25 19:05'

# 入力
try:
    with open("D019", "r", encoding="UTF-8") as inp_txt:
        for i in inp_txt:
            s, n = i.strip().split()
        inp_txt.close()

except FileNotFoundError:
    s, n = input().split()

# print(s, n)

# 処理
print(s[int(n) - 1: int(n)])

