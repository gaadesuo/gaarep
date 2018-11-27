#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/25 19:29'

# 入力
try:
    with open("D021", "r", encoding="UTF-8") as inp_txt:
        s_0, s_1 = [i.strip() for i in inp_txt]
        inp_txt.close()

except FileNotFoundError:
    s_0 = input()
    s_1 = input()

# print(s_0, s_1)

# 処理
print("Yes" if s_0 == s_1 else "No")