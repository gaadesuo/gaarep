# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2018/03/17 $'


txt_list = []
paiza = 0
try:
    with open("D005", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたデータは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

if paiza == 1:
    inp_num = [int(num) for num in input().split()]
else:
    inp_num = [int(num) for num in txt_list[0].split()]

# print("入力された数字は【{}】です".format(inp_num))
ans_list = [str(ans_num) for ans_num in range(inp_num[0], inp_num[0] + inp_num[1] * 10, inp_num[1])]
print(" ".join(ans_list))