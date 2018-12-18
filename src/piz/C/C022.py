#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/05 08:49'


# 入力
date_list = [[], [], [], []]
t_list = []

try:
    with open("C022", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt)
        inp_txt.close()
        for l in t_list[1:]:
            n_list = [int(i) for i in l.split()]
            for i in range(4):
                date_list[i].append(n_list[i])

except FileNotFoundError:
    for i in range(int(input())):
        n_list = [int(i) for i in input().split()]
        for i in range(4):
            date_list[i].append(n_list[i])

# print(date_list)

# 処理
print("{} {} {} {}".format(date_list[0][0], date_list[1][-1], max(date_list[2]), min(date_list[3])))