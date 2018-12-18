#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/05 08:46'

# 入力
n_list = []
try:
     with open("C020", "r", encoding="UTF-8") as inp_txt:
         for txt in inp_txt:
            n_list = [int(i) for i in txt.split()]
         inp_txt.close()

except FileNotFoundError:
    n_list = [int(i) for i in input().split()]

# print("元の重量, 一次加工%, 二次加工% {}".format(n_list))

# 処理
fast = n_list[0] - (n_list[0] * n_list[1] * 0.01)
print(fast - (fast * n_list[2] * 0.01))