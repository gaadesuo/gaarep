#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/03 20:03'

# 入力
s = ""

try:
    with open("C016","r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            s = txt
        inp_txt.close()

except FileNotFoundError:
    s = input()

# print(s)

# 処理
w = ["A", "E", "G", "I", "O", "S", "Z"]
n = ["4", "3", "6", "1", "0", "5", "2"]
for i in range(len(w)):
    s = s.replace(w[i], n[i])

print(s)