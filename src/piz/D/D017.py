#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/25 18:56'

# 入力
try:
    with open("D017", "r", encoding="UTF-8") as inp_txt:
        num_l = [int(s.strip()) for s in inp_txt]
        inp_txt.close()

except FileNotFoundError:
    num_l = [int(input()) for i in range(5)]

# print(num_l)

# 処理
print(max(num_l))
print(min(num_l))