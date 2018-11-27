#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/27 10:19'

# 入力
t_l = []
n0_l = []
n1_l = []
try:
    with open("D042", "r", encoding="UTF-8") as inp_txt:
        for i_0 in inp_txt:
            for i_1 in i_0.strip().split("\n"):
                t_l.append(i_1)
        inp_txt.close()
        n0_l = [int(i) for i in t_l[0].split()]
        n1_l = [int(i) for i in t_l[1].split()]

except FileNotFoundError:
    pass

print(n0_l, n1_l)