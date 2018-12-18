#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = "2018/12/15 17:21"

# 入力
long_list = []
t_list = []

try:
    with open("C040", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list = txt.split()
            long_list.append(t_list)
        inp_txt.close()
    del long_list[0]

except FileNotFoundError:
    for i in range(int(input())):
        t_list = input().split()
        long_list.append(t_list)

# print(long_list)

# 処理
le_list = []
ge_list = []

for l in long_list:
    if l[0] == "le":
        le_list.append(float(l[1]))
    else:
        ge_list.append(float(l[1]))

print("{} {}".format(max(ge_list), min(le_list)))

