# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = "2018/03/21"


txt_list = []
paiza = 0

try:
    with open("D024", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたデータは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

if paiza == 1:
    num_1 = int(input())
    num_2 = int(input())
else:
    num_1 = int(txt_list[0])
    num_2 = int(txt_list[1])

print(180 - (num_1 + num_2))