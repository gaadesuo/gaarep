#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/29 10:49'

# 入力
n = 0
try:
    with open("D052", "r", encoding="UTF-8")as inp_txt:
        for i in inp_txt:
            n = int(i)
        inp_txt.close()

except FileNotFoundError:
    n = int(input())

# print(n)

# 処理
ans = 0
for i in range(n + 1):
    ans += i

print(ans)