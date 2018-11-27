#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/27 09:18'

# 入力
num_l = []
try:
    with open("D041", "r", encoding="UTF-8") as inp_txt:
        for i_0 in inp_txt:
            num_l = [int(i_1) for i_1 in i_0.split()]
        inp_txt.close()

except FileNotFoundError:
    num_l = [int(i) for i in input().split()]

# print(num_l)

# 処理
print("OK" if num_l[2] * num_l[1] >= num_l[0] else "NG")