#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/01 19:02'

# 入力
s = ""
try:
    with open("D079", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            s = txt
        inp_txt.close()

except FileNotFoundError:
    s = input()

# print(s)

# 処理
ans = s[:1] * len(s)
# print(ans)
print("NG" if ans == s else "OK")