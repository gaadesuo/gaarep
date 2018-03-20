# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = "2018 / 03 / 20"


txt_list = []
paiza = 0
try:
    with open("D015", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたデータは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

inp_num = int(input()) if paiza == 1 else int(txt_list[0])
# print("入力された数字は【{}】です".format(inp_num))
for ans in range(inp_num, 0, -1):
    print(ans)