#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/05 08:44'

# 入力
n = 0
n_list = []
t_list = []

try:
    with open("C019", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt)
        inp_txt.close()
        n_list = [int(i) for i in t_list[1:]]

except FileNotFoundError:
    n_list = [int(input()) for i in range(int(input()))]

# print("チェックする数字のリスト: {}".format(n_list))

# 処理
nat_num = []
for i in n_list:
    nat_num = [j for j in range(1, i) if i % j == 0]
    # print(nat_num)
    print("perfect" if sum(nat_num) == i else "nearly" if (sum(nat_num) + 1) == i else "neither")