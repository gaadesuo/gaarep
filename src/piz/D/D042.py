# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/22'


txt_list = []
paiza = 0
try:
    with open("D042", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたデータは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

if paiza == 1:
    inp_num_1 = [int(num) for num in input().split()]
    inp_num_2 = [int(num) for num in input().split()]
else:
    inp_num_1 = [int(num) for num in txt_list[0].split()]
    inp_num_2 = [int(num) for num in txt_list[1].split()]

# print("入力された数字は【{}】と【{}】です".format(inp_num_1, inp_num_2))
print((inp_num_1[0] * inp_num_2[1]) - (inp_num_1[1] * inp_num_2[0]))