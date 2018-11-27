#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/26 11:28'

# 入力
n_0 = 0
n_1 = 0
try:
    with open("D037", "r", encoding="UTF-8") as inp_txt:
        n_0, n_1 = [int(i.strip()) for i in inp_txt]
        inp_txt.close()

except FileNotFoundError:
    n_0 = int(input())
    n_1 = int(input())

# print(n_0, n_1)

# 処理
print(-(-n_1 // n_0)) # 切り捨て算を負にしてやることにより切り上げになる
