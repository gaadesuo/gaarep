#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/25 18:00'

# 入力
try:
    with open("D016", "r", encoding="UTF-8") as inp_txt:
        s, n =[s.strip() for s in inp_txt]
        inp_txt.close()

except FileNotFoundError:
    s = input()
    n = input()

# print(s, n)

# 処理
print(s[:int(n)])