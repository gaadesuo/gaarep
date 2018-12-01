#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/01 18:24'

n_list = []
try:
    with open("D077", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            n_list = [int(n) for n in txt.split()]
        inp_txt.close()

except FileNotFoundError:
    n_list = [int(n) for n in input().split()]

# print(n_list)

# 処理
ans = n_list[1] * n_list[0]
print(ans if ans < 10000 else "NG")