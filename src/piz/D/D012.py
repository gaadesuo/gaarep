#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/25 17:08'

# ファイルから入力
inp_l =[]
paiza = 0

try:
    with open("D012", "r", encoding="UTF-8") as inp_txt:
        inp_l = [s.strip() for s in inp_txt]
        # print(inp_l)
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

# 処理
if paiza == 1:
    inp_l = [input()]
print(abs(int(inp_l[0])))