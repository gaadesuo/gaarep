#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/26 10:45'

# 入力
n = 0
try:
    with open("D034", "r", encoding="UTF-8") as inp_txt:
        for i in inp_txt:
            n = int(i.strip())
        inp_txt.close()

except FileNotFoundError:
    n = int(input())

# print(n)

# 処理
print(n if 21 % n == 0 else 21 % n)
