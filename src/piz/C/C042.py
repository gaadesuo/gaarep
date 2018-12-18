#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/17 01:39'

# 入力
vs_list = []
t_list = []

try:
    with open("C042", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list = [int(i) for i in txt.split()]
            vs_list.append(t_list)
        inp_txt.close()
    count_num = vs_list.pop(0)[0]

except FileNotFoundError:
    count_num = int(input())
    for i in range(int(((count_num ** 2) - count_num) / 2)):
        t_list = [int(i) for i in input().split()]
        vs_list.append(t_list)

# print("勝ち: 負け {}".format(vs_list))

# 処理
win_lose_list = []
for i in range(count_num):
    t_list = []
    for j in range(count_num):
        t_list.append("-")
    win_lose_list.append(t_list)
# print(win_lose_list)

for l in vs_list:
    win_lose_list[l[0] - 1][l[1] - 1] = "W"
    win_lose_list[l[1] - 1][l[0] - 1] = "L"

# print(win_lose_list)
for l in win_lose_list:
    print(" ".join(l))