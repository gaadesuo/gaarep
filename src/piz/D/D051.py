#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/29 10:32'

# 入力
w_list = []
try:
    with open("D051", "r", encoding="UTF-8") as inp_txt:
        for i in inp_txt:
            w_list = i.split()
        inp_txt.close()

except FileNotFoundError:
    w_list = input().split()

# print(w_list)

# 処理
print("OK" if w_list.count("W") > 4 else "NG")