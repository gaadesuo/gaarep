#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/26 11:11'

# 入力
s = ""
try:
    with open("D036", "r", encoding="UTF-8") as inp_txt:
        for i in inp_txt:
            s = i.strip()
        inp_txt.close()

except FileNotFoundError:
    s = input()

# print(s)

# 処理
print(s.replace("at", "@"))