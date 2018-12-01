#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/30 22:55'

# 入力
s = ""
try:
    with open("D073", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            s = txt
        inp_txt.close()

except FileNotFoundError:
    s = input()

# print(s)

# 処理
print(s[::-1])