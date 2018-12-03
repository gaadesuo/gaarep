#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/02 20:06'

import re

# 入力
hate_no = ""
room = 0
room_no_list = []
t_list = []

try:
    with open("C013", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt.strip())
        inp_txt.close()
        hate_no = t_list.pop(0)
        room = int(t_list.pop(0))
        room_no_list = t_list.copy()

except FileNotFoundError:
    hate_no = input()
    for i in range(int(input())):
        s = input()
        room_no_list.append(s)

# print("嫌いな番号: {}".format(hate_no))
# print("部屋番号リスト: {}".format(room_no_list))

# 処理
ans_list = []
hate_no_regex = re.compile(hate_no)
for no in room_no_list:
    if not(hate_no_regex.search(no)):
        ans_list.append(no)

if len(ans_list) == 0:
    print("none")

else:
    for i in ans_list:
        print(i)