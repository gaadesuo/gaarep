#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/25 10:24'

# ファイルから取り込み
txt_l = []
paiza = 0
try:
    with open("D010", "r", encoding="UTF-8") as inp_txt:
        txt_l = [s.strip() for s in inp_txt]
        # print(txt_l)
        inp_txt.close()

except FileNotFoundError:
    paiza = 1

# 処理
if paiza == 1:
    txt_l = [input() for i in range(2)]

print("{}@{}".format(txt_l[0], txt_l[1]))