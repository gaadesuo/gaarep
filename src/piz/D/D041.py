# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2018/04/04'

txt_list = []
paiza = 0

try:
    with open("D041", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたデータは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

if paiza == 1:
    inp_list = [int(num) for num in input().split()]
else:
    inp_list = [int(num) for num in txt_list[0].split()]
# print("本の幅は【{}】、本棚の段数は【{}】、一段の幅は【{}】です".format(inp_list[0], inp_list[1], inp_list[2]))
print("OK" if inp_list[0] < (inp_list[1] * inp_list[2]) else "NG")