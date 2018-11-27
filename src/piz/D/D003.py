#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/25 06:23'

# ファイルから入力
txt_list =[]
paiza = 0
try:
    with open("D003", "r", encoding="UTF-8") as inp_txt:
        txt_list = [i.strip() for i in inp_txt]
        # print(txt_list)
        inp_txt.close()

except FileNotFoundError:
    paiza = 1

# 処理
n = int(input()) if paiza == 1 else int(txt_list[0])
# print(n)
ans_list = [str(n * i) for i in range(1, 10)]
print(" ".join(ans_list))
