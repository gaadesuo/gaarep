#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/30 13:42'

# 入力
n = 0
try:
    with open("D067", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            n = int(txt)
        inp_txt.close()

except FileNotFoundError:
    n = int(input())

# print(n)

# 処理
print("OFF" if n % 2 == 0 else "ON")