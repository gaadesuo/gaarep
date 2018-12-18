#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/11 12:08'

import collections

# 入力
standard_t_dic = {}
# 入力順に並べる辞書の作成
time_dic = collections.OrderedDict()
standard_country = ""
t_list = []

# 入力
try:
    with open("C031", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list = txt.split()
            if len(t_list) > 1:
                if t_list[1].count(":") > 0:
                    standard_country = t_list[0]
                    standard_t_dic[t_list[0]] = [int(i) for i in t_list[1].split(":")]
                else:
                    time_dic[t_list[0]] = int(t_list[1])
        inp_txt.close()

except FileNotFoundError:
    for i in range(int(input())):
        t_list = input().split()
        time_dic[t_list[0]] = int(t_list[1])
    t_list = input().split()
    standard_country = t_list[0]
    standard_t_dic[t_list[0]] = [int(i) for i in t_list[1].split(":")]

# print("標準国: 標準時間 {}".format(standard_t_dic))
# print("国名: 時差リスト {}".format(time_dic))

# 処理
# 現在時刻から時差を引いて現在の基準時間を求める
standard_time = standard_t_dic[standard_country][0] - time_dic[standard_country]
# print("基準時間: {}".format(standard_time))

for v in time_dic.values():
    print("{:02d}:{:02d}".format((standard_time + v) % 24, standard_t_dic[standard_country][1]))