# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2017 / 12 / 23

txt_list = []

try:
    with open("C31", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたテキストは: {}".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    pass

time_list = []
if len(txt_list) == 0:
    for lp0 in range(int(input())):
        time = input().split()
        time_list.append(time)
else:
    for index in range(1, int(txt_list[0]) + 2):
        time_list.append(txt_list[index].split())

# print("入力されたデーターは: {}".format(time_list))

# 標準時間と基準国の時差から現在時間を求める
standard_time = list(map(int, time_list[-1][1].split(":")))
standard_country = time_list[-1][0]
# print("標準時間は {:02d}:{:02d}".format(standard_time[0], standard_time[1]))
del time_list[-1]
temp_time = [int(diff_time) for country, diff_time in time_list if country == standard_country]
# 標準時間に基準国の時差を足して基準時間を求める
ans_time = standard_time[0] + temp_time[0]
# print("基準国である{}の現在時刻は{:0d}時".format(standard_country, ans_time))

for time in time_list:
    change_time = ans_time + (standard_time[0] + int(time[1]))
    if change_time < 0:
        change_time += 24
    elif change_time > 23:
        change_time -= 24
    print("{:02d}:{:02d}".format(change_time, standard_time[1]))
