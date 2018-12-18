#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/14 00:04'

# 入力
time_date = ""

try:
    with open("C037", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            time_date = txt.strip()
        inp_txt.close()

except FileNotFoundError:
    time_date = input()

# print(time_date)

# 処理
t_list = time_date.split()
day = [int(i) for i in t_list[0].split("/")]
time = [int(i) for i in t_list[1].split(":")]
# print(day, time)
if time[0] > 23:
    day[1] += int(time[0] / 24)
    time[0] %= 24

print("{:02d}/{:02d} {:02d}:{:02d}".format(day[0], day[1], time[0], time[1]))