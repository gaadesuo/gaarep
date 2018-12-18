#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/08 18:06'

# 周力
date_list = []
day_list = []
t_list = []

try:
    with open("C029", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt)
        inp_txt.close()
    date_list = [int(i) for i in t_list.pop(0).split()]
    for l in t_list:
        n_list = [int(i) for i in l.split()]
        day_list.append(n_list)

except FileNotFoundError:
    date_list = [int(i) for i in input().split()]
    for i in range(date_list[0]):
        n_list = [int(i) for i in input().split()]
        day_list.append(n_list)

# print("日にち: 日数 {}".format(date_list))
# print("日: 降水確率 {}".format(day_list))

# 処理
rainy = 0
last_day = date_list[0] - (date_list[1] - 1)
rainy_list = []
for i in range(0, last_day):
    for j in range(date_list[1]):
        # print(day_list[i + j][1])
        rainy += day_list[i + j][1]
    rainy_list.append(rainy / date_list[1])
    rainy = 0
# print(rainy_list)
fast_index = rainy_list.index(min(rainy_list))

print("{} {}".format(day_list[fast_index][0], day_list[fast_index][0] + date_list[1] - 1))
