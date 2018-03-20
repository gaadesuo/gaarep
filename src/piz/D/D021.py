# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = "2018/03/20"


txt_list = []
paiza = 0
try:
    with open("D021", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたデータは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

if paiza == 1:
    word_1 = input()
    word_2 = input()
else:
    word_1 = txt_list[0]
    word_2 = txt_list[1]
# print("入力された文字は【{}】と【{}】です".format(word_1, word_2))
print("Yes" if word_1 == word_2 else "No")