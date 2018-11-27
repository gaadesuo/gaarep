#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/25 17:22'

# ファイルから入力
inp_l = []

try:
    with open("D013", "r", encoding="UTF-8") as inp_txt:
        inp_l = [s.strip() for s in inp_txt]
        inp_txt.close()

except FileNotFoundError:
    inp_l = [input()]
# print(inp_l)

# 処理
n_0, n_1 = [int(i) for i in inp_l[0].split()]
s, a = divmod(n_0, n_1)
print("{} {}".format(s, a))