#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/25 08:12'

# ファイルから入力
txt_l = []
paiza = 0

try:
    with open("D007", "r", encoding="UTF-8") as inp_txt:
        txt_l = [s.strip() for s in inp_txt]
        # print(txt_l)
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

# 処理
if paiza == 1:
    n = int(input())
else:
    n = int(txt_l[0])
print("*" * n)
