#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/14 11:14'

# 入力
date_list = []
allo_list = []
t_list = []

try:
    with open("C038", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt)
        inp_txt.close()
    date_list = [int(i) for i in t_list.pop(0).split()]
    allo_list = [int(i) for i in t_list]

except FileNotFoundError:
    date_list = [int(i) for i in input().split()]
    for i in range(date_list[0]):
        allo_list.append(int(input()))

# print("機械の数: お菓子の数: {}".format(date_list))
# print("各々の機械の分配数: {}".format(allo_list))

# 処理
rem_list = []
index_list = []
min_rem_box = []

for i in allo_list:
    rem_list.append(date_list[1] % i)
# print("各々のお菓子のあまり {}".format(rem_list))

min_rem = min(rem_list)

if rem_list.count(min_rem) > 1:
    index_list = [i for i, x in enumerate(rem_list) if x == min_rem]
    # print(index_list)
    for i in index_list:
        min_rem_box.append(allo_list[i])
    print(allo_list.index((max(min_rem_box))) + 1)
else:
    print(rem_list.index(min_rem) + 1)