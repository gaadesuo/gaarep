#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/30 14:00'

# 入力
n_list = []
try:
    with open("D069", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            n_list = [int(i) for i in txt.split()]
        inp_txt.close()

except FileNotFoundError:
    n_list = [int(i) for i in input().split()]

# print(n_list)

# 処理
rou = lambda x: (((x * 10) * 2 + 1) // 2) / 10

total = sum(n_list)
print("{:.1f}".format(rou(total / len(n_list))))
