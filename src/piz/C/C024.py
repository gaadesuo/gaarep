#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/06 07:04'

# 入力
ctr_list = []
t_list = []

try:
    with open("C024", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt.strip())
        inp_txt.close()
    for l in t_list[1:]:
        ctr_list.append(l.split())

except FileNotFoundError:
    for i in range(int(input())):
        t_list = input().split()
        ctr_list.append(t_list)

# print(ctr_list)

# 処理
var_1 = 0
var_2 = 0

for l in ctr_list:
    if l[0] == "SET":
        if l[1] == "1":
            var_1 = int(l[2])
        else:
            var_2 = int(l[2])
    elif l[0] == "ADD":
        var_2 = var_1 + int(l[1])
    elif l[0] == "SUB":
        var_2 = var_1 - int(l[1])

print("{} {}".format(var_1, var_2))