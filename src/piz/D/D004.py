#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/25 06:58'

# ファイルから入力
txt_list = []
paiza = 0
try:
    with open("D004", "r", encoding="UTF-8") as inp_txt:
        txt_list = [i.strip() for i in inp_txt]
        # print(txt_list)
        inp_txt.close()

except FileNotFoundError:
    paiza = 1

# 処理

if paiza == 1:
    print_list = [input() for i in range(int(input()))]
else:
    print_list = [txt_list[i + 1] for i in range(int(txt_list[0]))]

# print(print_list)

print("Hello " + ",".join(print_list) + ".")
