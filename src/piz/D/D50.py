#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/29 10:17'

# 入力
n_list = []
try:
    with open("D050", "r", encoding="UTF-8") as inp_txt:
        for i in inp_txt:
            n_list = [int(n) for n in i.strip().split()]
        inp_txt.close()

except FileNotFoundError:
    n_list = [int(n) for n in input().split()]

# print(n_list)

# 処理
ans = 0
for i in n_list:
    if i > 5:
        ans += 5
    else:
        ans += i
print(ans)