#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/03 20:02'

# 入力
n = 0
date_list = []
t_list = []

try:
    with open("C015", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt)
        inp_txt.close()
        n = int(t_list.pop(0))
        for i in t_list:
            n_list = [int(j) for j in i.split()]
            date_list.append(n_list)

except FileNotFoundError:
    for i in range(int(input())):
        n_list = [int(j)  for j in input().split()]
        date_list.append(n_list)

# print(date_list)

# 処理
point = 0
for l in date_list:
    if l[0] % 10 == 3 or int(l[0] / 10) == 3:
        point += int(l[1] * 0.03)
    elif l[0] % 10 == 5:
        point += int(l[1] * 0.05)
    else:
        point += int(l[1] * 0.01)

print(point)
