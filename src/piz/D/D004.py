# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2018/03/17 $'


txt_list = []
paiza = 0
try:
    with open("D004", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたデータは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

inp_word = []
if paiza == 1:
    inp_word = [input() for lp0 in range(int(input()))]
else:
    inp_word = [txt_list[index_num + 1]for index_num in range(int(txt_list[0]))]
# print("入力された文字は【{}】です".format(inp_word))

print("Hello " + ",".join(inp_word) + ".")
