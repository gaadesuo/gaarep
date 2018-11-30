#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/30 08:39'

# 入力
n_list = []
try:
    with open("D062", "r", encoding="UTF-8") as inp_txt:
        for i in inp_txt:
            n_list =[int(n) for n in i.split()]
        inp_txt.close()

except FileNotFoundError:
    n_list = [int(n) for n in input().split()]

# print(n_list)

# 処理
w = "ABCDEFGHIJ"
print("""{}
{}
{}""".format(w[0:n_list[0]],
             w[n_list[0]:n_list[0] + n_list[1]],
             w[n_list[0] + n_list[1]:n_list[0] + n_list[1] + n_list[2]]))