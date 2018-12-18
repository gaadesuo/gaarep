#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/08 03:11'

# 入力
word_list = []
t_list = []

try:
    with open("C028", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt.strip())
        inp_txt.close()
    for l in t_list[1:]:
        s_list = l.split()
        word_list.append(s_list)

except FileNotFoundError:
    for i in range(int(input())):
        s_list = input().split()
        word_list.append(s_list)

# print("正解: 回答: {}".format(word_list))

# 処理
point = 0
for l in word_list:
    if l[0] == l[1]:
        point += 2
    elif len(l[0]) == len(l[1]):
        if sum(l[0][i] != l[1][i] for i in range(len(l[0]))) == 1:
            point += 1

print(point)


