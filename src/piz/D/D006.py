# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2018/03/17 $'


txt_list = []
paiza = 0

try:
    with open("D006", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたデータは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

if paiza == 1:
    inp_word = input().split()
else:
    inp_word = txt_list[0].split()

# print("入力された距離は【{}】です".format(inp_word))
print(int(inp_word[0]) * 1000000 if inp_word[1] == "km" else
      int(inp_word[0]) * 1000 if inp_word[1] == "m" else
      int(inp_word[0]) * 10)
