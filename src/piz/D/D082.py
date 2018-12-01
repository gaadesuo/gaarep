#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/01 19:53'

# 入力
w_list = []
try:
    with open("D082", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            w_list.append(txt.strip())
        inp_txt.close()

except FileNotFoundError:
    w_list = [input() for i in range(2)]

# print(w_list)

print("NG" if w_list[0][-1:] != w_list[1][:1] or w_list[1][-1:] == "n" else "OK")