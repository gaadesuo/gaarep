# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = "2018 / 03 / 20"


txt_list = []
paiza = 0

try:
    with open("D017", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたデーターは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

if paiza == 1:
    inp_num = [int(input()) for lp0 in range(5)]
else:
    inp_num = list(map(int, txt_list))
# print("入力された数字のリストは【{}】です".format(inp_num))
print(max(inp_num))
print(min(inp_num))