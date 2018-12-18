#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/13 09:55'

# 入力
vs_date = []
fast_time = []
second_time = []
t_list = []

try:
    with open("C036", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            s_list = txt.strip().split()
            t_list.append(s_list)
        inp_txt.close()
    for i in range(2):
        for j in t_list.pop(0):
            vs_date.append(int(j))
    fast_time = [int(i) for i in t_list[0]]
    second_time = [int(i) for i in t_list[1]]

except FileNotFoundError:
    for i in range(2):
        for j in input().split():
            vs_date.append(int(j))
    fast_time = [int(i) for i in input().split()]
    second_time = [int(i) for i in input().split()]

# print("一回戦: {}".format(vs_date))
# print("一回戦のtime: {}".format(fast_time))
# print("決勝のtime: {}".format(second_time))

# 処理
win = []


def winner(l, n_0, n_1): return n_0 if l[n_0 - 1] < l[n_1 - 1] else n_1


win.append(winner(fast_time, vs_date[0], vs_date[1]))
win.append(winner(fast_time, vs_date[2], vs_date[3]))
sort_win = sorted(win)
# print(sort_win)
if second_time[0] < second_time[1]:
    print(sort_win[0], sort_win[1], sep="\n")
else:
    print(sort_win[1], sort_win[0], sep="\n")
