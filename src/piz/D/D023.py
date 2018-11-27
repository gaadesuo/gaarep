#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/25 19:59'

# 入力
try:
    with open("D023", "r", encoding="UTF-8") as inp_txt:
        for i in inp_txt:
            s = i
        inp_txt.close()

except FileNotFoundError:
    s = input()

# print(s)

# 処理
print(s.count("A"))