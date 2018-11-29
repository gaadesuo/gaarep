#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/29 10:01'

# 入力
w = ""
try:
    with open("D049", "r", encoding="UTF-8") as inp_txt:
        for i in inp_txt:
            w = i
        inp_txt.close()

except FileNotFoundError:
    w = input()

# print(w)

# 処理
print(w[:-5] if "noaki" in w else w)