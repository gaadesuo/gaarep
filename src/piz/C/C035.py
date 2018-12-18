#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/13 00:57'

# 入力
date_list = []
t_list = []

try:
    with open ("C035", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list = txt.split()
            date_list.append(t_list)
        inp_txt.close()
    del date_list[0]

except FileNotFoundError:
    for i in range(int(input())):
        t_list = input().split()
        date_list.append(t_list)

# print(date_list)

# 処理
passing = 0
for l in date_list:
    subject = l.pop(0)
    point_list = [int(i) for i in l]
    if sum(point_list) >= 350:
        if subject == "s" and (point_list[1] + point_list[2]) >= 160:
            passing += 1
        elif subject == "l" and (point_list[3] + point_list[4]) >= 160:
            passing += 1

print(passing)