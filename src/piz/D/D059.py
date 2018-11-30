#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/30 07:57'

# 入力
w_list = []
try:
    with open("D059", "r", encoding="UTF-8") as inp_txt:
        for i in inp_txt:
            w_list = i.strip().split()
        inp_txt.close()

except FileNotFoundError:
    w_list = input().split()

# print(w_list)

# 処理
print("{} Q".format(w_list[0]) if "J" is w_list[0] is w_list[1] else
      "{} {}".format(w_list[0], w_list[1]))