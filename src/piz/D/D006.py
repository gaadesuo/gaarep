#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/25 07:58'

# ファイルから入力
txt_list =[]
paiza = 0
try:
    with open("D006", "r", encoding="UTF-8") as inp_txt:
        txt_list = [s.strip() for s in inp_txt]
        # print(txt_list)
        inp_txt.close()

except FileNotFoundError:
    paiza = 1

# 処理
if paiza == 1:
    inp_l = input().split()
else:
    inp_l = txt_list[0].split()
# print(inp_l)
print(int(inp_l[0]) * 10 if inp_l[1] == "cm" else
      int(inp_l[0]) * 1000 if inp_l[1] == "m" else
      int(inp_l[0]) * 1000000)