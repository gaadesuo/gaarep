#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = "2018/12/15 16:26"

# 入力
word_list = []

try:
    with open("C039", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            word_list = txt.split("+")
        inp_txt.close()

except FileNotFoundError:
    word_list = input().split("+")

# print(word_list)

# 処理
ten = 0
one = 0
for l in word_list:
    ten += l.count("<")
    one += l.count("/")

print((ten * 10) + one)