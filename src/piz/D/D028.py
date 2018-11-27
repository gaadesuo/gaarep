#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/26 09:40'

# 入力
s = ""
try:
    with open("D028", "r", encoding="UTF-8") as inp_txt:
        for i in inp_txt:
            s = i
        inp_txt.close()

except FileNotFoundError:
    s = input()

# print(s)

# 処理
print(len(s))