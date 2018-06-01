# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2018/03/29'

txt_list = []
paiza = 0
try:
    with open("D033", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        print("入力されたデータは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

inp_word_list = input().split() if paiza == 1 else txt_list[0].split()
print("入力された名前は【{}】です".format(inp_word_list))
print("{}.{}".format(inp_word_list[0][0:1], inp_word_list[1][0:1]))