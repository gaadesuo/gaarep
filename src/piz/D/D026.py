# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2018/03/22'

txt_list = []
paiza = 0

try:
    with open("D026", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたデータは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

inp_word = []
if paiza == 1:
    for lp0 in range(7):
        inp_word.append(input())
else:
    inp_word = txt_list
# print("入力された文字のリストは【{}】".format(inp_word))
print(inp_word.count("no"))