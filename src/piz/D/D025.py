#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/25 21:28'

# 入力
try:
    with open("D025", "r", encoding="UTF-8") as inp_txt:
        for i in inp_txt:
            n = int(i)
        inp_txt.close()

except FileNotFoundError:
    n = int(input())

# print(n)

# 処理
print("{:03d}".format(n))