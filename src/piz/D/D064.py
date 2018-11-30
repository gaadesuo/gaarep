#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/30 09:45'

# 入力
w = ""
try:
    with open("D064", "r", encoding="UTF-8") as inp_txt:
        for i in inp_txt:
            w = i
        inp_txt.close()

except FileNotFoundError:
    w = input()

# print(w)

# 処理
print(w.replace("False", "True"))