#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/19 19:50'

# 入力
no_list = []

try:
    with open("B012", "r", encoding="UTF-8") as inp_txt:
        next(inp_txt)
        for txt in inp_txt:
            no_list.append(txt.strip())
        inp_txt.close()

except FileNotFoundError:
    for i in range(int(input())):
        no_list.append(input())

# print("クレカNOリスト: {}".format(no_list))

# 処理
for l in no_list:
    even = 0
    odd = 0
    t_list = list(map(int, l[:-1]))
    # print(t_list)
    for i in range(0, 15, 2):
        if t_list[i] > 4:
            even += int((t_list[i] * 2) / 10) + ((t_list[i] * 2) % 10)
        else:
            even += t_list[i] * 2
    for i in range(1, 15, 2):
        odd += t_list[i]
    # print(even, odd)
    print("0" if ((even + odd) % 10) == 0 else (10 - (even + odd) % 10))