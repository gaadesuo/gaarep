#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/26 09:33'

# 入力
try:
    with open("D027", "r", encoding="UTF-8") as inp_txt:
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
