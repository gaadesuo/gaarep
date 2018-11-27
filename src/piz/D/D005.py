#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/25 07:23'

# ファイルから入力
txt_list = []
paiza = 0
try:
    with open("D005", "r", encoding="UTF-8") as inp_txt:
        txt_list = [s.strip() for s in inp_txt]
        # print(txt_list)
        inp_txt.close()

except FileNotFoundError:
    paiza = 1

# 処理
if paiza == 1:
    n, c = [int(i) for i in input().split()]
else:
    n, c = [int(i) for i in txt_list[0].split()]
# print(n, c)
print_l = [str(i) for i in range(n, n + c * 10, c)]
# print(print_l)
print(" ".join(print_l))