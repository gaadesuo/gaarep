#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/26 11:04'

# 入力
s_l = []
try:
    with open("D035", "r", encoding="UTF-8") as inp_txt:
        for i in inp_txt:
            s_l = i.strip().split()
        inp_txt.close()

except FileNotFoundError:
    s_l = input().split()

# print(s_l)

# 処理
print("{}/{}/{}".format(s_l[0], s_l[1], s_l[2]))