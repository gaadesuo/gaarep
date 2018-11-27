#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/25 21:40'

# 入力
try:
    with open("D026", "r", encoding="UTF-8") as inp_txt:
        word_l = [s.strip() for s in inp_txt]
        inp_txt.close()

except FileNotFoundError:
    word_l = [input() for i in range(7)]

# print(word_l)

# 処理
print(word_l.count("no"))