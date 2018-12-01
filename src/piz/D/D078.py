#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/01 18:47'

# 入力
t_list = []
n_list = []
n = 0

try:
    with open("D078", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt)
        inp_txt.close()
        n_list = [int(i) for i in t_list[0].split()]
        n = int(t_list[1])

except FileNotFoundError:
    n_list = [int(i) for i in input().split()]
    n = int(input())

# print(n_list, n)

# 処理
ave = sum(n_list) / len(n_list)
print("pass" if ave >= n else "failure")