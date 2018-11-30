#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/30 13:49'

# 入力
t_list = []
n = ""
s = ""
try:
    with open("D068", "r", encoding="UTF-8") as inp_txt:
        t_list = [txt.strip() for txt in inp_txt]
        n, s = t_list

except FileNotFoundError:
    n = input()
    s = input()

# print(n, s)

# 処理
s_count = s.count("S")
print("{} {}".format(s_count, (int(n) - s_count)))