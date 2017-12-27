# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ =  2017 / 11 / 28

# テキストから入力
txt_list = []
try:
    with open("C39", "r", encoding="utf-8") as inp_txt:
        txt_list = [word.strip() for word in inp_txt]
        # print("入力されたテキストは: {}".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    pass

if len(txt_list) == 0:
    inp_word = input().split("+")
else:
    inp_word = txt_list[0].split("+")

# print("入力された文字リスト{}".format(inp_word))
ans = 0
for n_word in inp_word:
    ans += n_word.count("/")
    ans += (n_word.count("<") * 10)

print(ans)