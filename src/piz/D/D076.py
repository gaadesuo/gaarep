#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/01 17:59'

# 入力
w_list = []
try:
    with open("D076", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            w_list.append(txt.strip())
        inp_txt.close()

except FileNotFoundError:
    for i in range(2):
        w_list.append(input())

# print(w_list)

# 処理
print("NG" if w_list[0] in w_list[1] else w_list[1])