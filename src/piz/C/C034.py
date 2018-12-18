#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/12 23:29'

# 入力
cal_list = []

try:
    with open("C034", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            cal_list = txt.split()
        inp_txt.close()

except FileNotFoundError:
    cal_list = input().split()

# print("左辺1: 左辺2: 右辺 {}".format(cal_list))

# 処理
x_index = cal_list.index("x")
arithmetic = cal_list[1]
# print(x_index, arithmetic)
if x_index == 0:
    print(int(cal_list[4]) - int(cal_list[2]) if arithmetic == "+" else
          int(cal_list[4]) + int(cal_list[2]))
elif x_index == 2:
    print(int(cal_list[4]) - int(cal_list[0]) if arithmetic == "+" else
          (int(cal_list[4]) - int(cal_list[0])) * -1)
else:
    print(int(cal_list[0]) + int(cal_list[2]) if arithmetic == "+" else
          int(cal_list[0]) - int(cal_list[2]))