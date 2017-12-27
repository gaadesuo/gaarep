# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = "2017/12/15"

txt_list = []
try:
    with open("C34", "r", encoding="utf-8") as inp_txt:
        txt_list = [word.strip() for word in inp_txt]
        # print("入力されたテキストは: {}".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    pass

if len(txt_list) == 0:
    inp_word = input().split()
else:
    inp_word = txt_list[0].split()
# print("入力された文字は: {}".format(inp_word))
# たし算の時
if inp_word[1] == "+":
    if inp_word[0] == "x":
        print(int(inp_word[4]) - int(inp_word[2]))
    elif inp_word[2] == "x":
        print(int(inp_word[4]) - int(inp_word[0]))
    else:
        print(int(inp_word[0]) + int(inp_word[2]))
else:
    if inp_word[0] == "x":
        print(int(inp_word[2]) + int(inp_word[4]))
    elif inp_word[2] == "x":
        print(int(inp_word[0]) - int(inp_word[4]))
    else:
        print(int(inp_word[0]) - int(inp_word[2]))