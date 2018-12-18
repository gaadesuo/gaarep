#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/17 18:57'

import collections

# 入力
used_list = []

try:
    with open("C043", "r", encoding="UTF-8") as inp_txt:
        next(inp_txt)
        for txt in inp_txt:
            used_list = [int(i) for i in txt.split()]

except FileNotFoundError:
    count_num = int(input())
    used_list = [int(i) for i in input().split()]

# print("アイテムを使用したIDリスト: {}".format(used_list))

# 処理
counter_dic = collections.Counter(used_list)
# print(counter_dic)
max_num = max(counter_dic.values())
max_id_list = [k for k, v in counter_dic.items() if v == max_num]
max_id_list.sort()
print(" ".join(list(map(str, max_id_list))))