#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/17 00:01'

# 入力
medal_list = []
t_list = []

try:
    with open("C041", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list = [int(i) for i in txt.split()]
            medal_list.append(t_list)
        inp_txt.close()
    del medal_list[0]

except FileNotFoundError:
    for i in range(int(input())):
        t_list = [int(i) for i in input().split()]
        medal_list.append(t_list)

# print("メダルリスト: {}".format(medal_list))

# 処理
medal_list.sort(reverse=True)
# print(medal_list)
for l in medal_list:
    print(" ".join(list(map(str, l))))