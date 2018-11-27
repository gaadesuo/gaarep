#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/25 17:36'

# 入力
try:
    with open("D014", "r", encoding="UTF8") as inp_txt:
        word_l = [s.strip() for s in inp_txt]
        inp_txt.close()

except FileNotFoundError:
    word_l = [input()]

# print(word_l)

# 処理
print(word_l[0].upper())