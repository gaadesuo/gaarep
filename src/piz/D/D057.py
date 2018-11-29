#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/29 11:43'

# 入力
n = 0
s = ""
w_list = []
try:
    with open("D057", "r", encoding="UTF-8") as inp_txt:
        n, s = [i.strip() for i in inp_txt]
        n = int(n)
        w_list = s.split()
        inp_txt.close()

except FileNotFoundError:
    n = int(input())
    w_list = input().split()

# print(n, w_list)

# 処理
print(w_list[n - 1])