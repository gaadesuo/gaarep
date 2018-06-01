# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/24$'

txt_list = []
paiza = 0
try:
     with open("D044", "r", encoding="utf-8") as inp_txt:
         txt_list = [txt.strip() for txt in inp_txt]
         # print("入力されたデータは【{}】です".format(txt_list))
         inp_txt.close()
except FileNotFoundError:
    paiza = 1

inp_word = input().split() if paiza == 1 else txt_list[0].split()
# print("入力された文字は【{}】です".format(inp_word))
if inp_word[1] == "F":
    print("Hi, Ms. {}".format(inp_word[0]))
else:
    print("Hi, Mr. {}".format(inp_word[0]))