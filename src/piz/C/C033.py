# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = "2017/12/16"

txt_list = []
try:
    with open("C33", "r", encoding="utf-8") as inp_txt:
        txt_list = [word.strip() for word in inp_txt]
        # print("入力されたテキストは: {}".format(txt_list))
    inp_txt.close()
except FileNotFoundError:
    pass

calls_list = []
if len(txt_list) == 0:
    calls_list = [input() for lp0 in range(int(input()))]
else:
    for index in range(1, int(txt_list[0]) + 1):
        c = txt_list[index]
        calls_list.append(c)
# print("入力されたカウントのリストは: {}".format(calls_list))
s = 0
b = 0
for call in calls_list:
    if call == "strike":
        s += 1
        if s == 3:
            print("out!")
        else:
            print("strike!")
    elif call == "ball":
        b += 1
        if b == 4:
            print("fourball!")
        else:
            print("ball!")
    else:
        print("error")