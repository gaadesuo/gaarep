#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/27 11:30'

w_l = []
try:
    with open("D044", "r", encoding="UTF-8") as inp_txt:
        for i in inp_txt:
            w_l = i.strip().split()
        inp_txt.close()

except FileNotFoundError:
    w_l = input().split()

# print(w_l)

# 処理
w_l[1] = "Ms" if w_l[1] == "F" else "Mr"
print("Hi, {}. {}".format(w_l[1], w_l[0]))