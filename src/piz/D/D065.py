#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/30 10:04'

# 入力
w = ""
try:
    with open("D065", "r", encoding="UTF-8") as inp_txt:
        for s in inp_txt:
            w = s
        inp_txt.close()
except FileNotFoundError:
    w = input()

# print(w)

# 処理
print("ok" if w[:-2] == "2" else
      "error" if w[:-2] == "4" else
      "unknown")