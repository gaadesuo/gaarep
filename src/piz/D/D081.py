#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/01 19:31'

# 入力
t_list = []
n_list = []
n = 0

try:
    with open("D081", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt)
        inp_txt.close()
        n_list = [int(i) for i in t_list[1].split()]
        n = int(t_list[0])

except FileNotFoundError:
    n = int(input())
    n_list = [int(i) for i in input().split()]

# print(n, n_list)

# 処理
print((n_list[0] * n_list[1]) % n)

