# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = "2017/12/13"


txt_list = []
try:
    with open("C37", "r", encoding="utf-8") as txt_date:
        txt_list = [word.strip() for word in txt_date]
        # print("入力されたテキストデータのリストは: {}".format(txt_list))
        txt_date.close()
except FileNotFoundError:
    pass

if len(txt_list) == 0:
    inp_date = input().split()
else:
    inp_date = txt_list[0].split()
day = list(map(int, inp_date[0].split("/")))
time = list(map(int, inp_date[1].split(":")))
# print("入力されたデータ。 {}月,{}日,{}時,{}分".format(day[0], day[1], time[0], time[1]))
counter = 0
while True:
    if time[0] < 24:
        break
    else:
        time[0] -= 24
        counter += 1
print("{:02d}/{:02d} {:02d}:{:02d}".format(day[0], day[1] + counter, time[0], time[1]))
