#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/27 11:16'

# 入力
n = 0
try:
    with open("D043", "r", encoding="UTF-8") as inp_txt:
        for i in inp_txt:
            n = int(i.strip())
        inp_txt.close()

except FileNotFoundError:
    n = int(input())

# print(n)

# 処理
print("sunny" if n <= 30 else
      "rainy" if n >= 71 else
      "cloudy")
