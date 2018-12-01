#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/01 00:49'

# 入力
n_set = set()
try:
    with open("D075", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            n_set.add(int(txt))
        inp_txt.close()

except FileNotFoundError:
    n_set = {int(input()) for i in range(4)}

# print(n_set)

# 処理
max_set = set(range(1, 6))
for i in (max_set - n_set):
    print(i)
