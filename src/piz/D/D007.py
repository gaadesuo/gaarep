# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2018 / 3 / 18


txt_list = []
paiza = 0

try:
    with open("D007", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたテキストは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

inp_num = 0
if paiza == 1:
    inp_num = int(input())
else:
    inp_num = int(txt_list[0])
# print("入力された数字は【{}】です".format(inp_num))
print("*" * inp_num)