#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/03 20:06'

# 入力
paernt = []
child_num = 0
child_list =[]
t_list = []

try:
    with open("C017", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt.strip())
        inp_txt.close()
        paernt = [int(i) for i in t_list.pop(0).split()]
        child_num = int(t_list.pop(0))
        for i in t_list:
            n_list = [int(j) for j in i.split()]
            child_list.append(n_list)

except FileNotFoundError:
    paernt = [int(i) for i in input().split()]
    for i in range(int(input())):
        n_list = [int(i) for i in input().split()]
        child_list.append(n_list)

# print("親のデータ: {}".format(paernt))
# print("子のデータリスト: {}".format(child_list))

# 処理
for l in child_list:
    if paernt[0] > l[0]:
        print("High")
    elif paernt[0] == l[0]:
        print("High" if paernt[1] < l[1] else "Low")

    else:
        print("Low")