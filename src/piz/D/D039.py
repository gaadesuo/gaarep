#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/27 09:39'

# 入力
n_0 = 0
n_1 = 0
n_2 = 0
try:
    with open("D039", "r", encoding="UTF-8") as inp_txt:
        n_0, n_1, n_2 = [int(i.strip()) for i in inp_txt]
        inp_txt.close()

except FileNotFoundError:
    n_0 = int(input())
    n_1 = int(input())
    n_2 = int(input())

# print(n_0, n_1, n_2)

# 処理
print("YES" if n_0 == n_1 == n_2 else "NO")