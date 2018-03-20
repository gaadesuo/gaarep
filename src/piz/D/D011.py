# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2018/03/18'


txt_list = []
paiza = 0

try:
    with open("D011", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたデータは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

# Aのアスキーコードを代入
ascii_A_num = ord("A")
# print("Aのアスキーコード番号は【{}】です".format(ascii_A_num))

if paiza == 1:
    inp_word = input()
else:
    inp_word = txt_list[0]

ascii_inp_word_num = ord(inp_word)
# print("入力された文字は【{}】でアスキーコードは【{}】です".format(inp_word, ascii_inp_word_num))
print((ascii_inp_word_num - ascii_A_num) + 1)

