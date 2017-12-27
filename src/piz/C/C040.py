# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = "2017/12/07"
import os

# テスト入力テキストの読み込み
read_txt = []
try:
    with open("C40", "r", encoding="utf-8") as inp_txt:
        read_txt = [txt.strip() for txt in inp_txt]
        # print("テスト入力テキストの中身は: {}".format(read_txt))
        inp_txt.close()
except FileNotFoundError:
    pass

# テスト入力txtがないならinput()入力
if len(read_txt) == 0:
    count_num = int(input())
else:
    count_num = int(read_txt[0])

le_list =[]
ge_list = []
for lp0 in range(count_num):
    if len(read_txt) == 0:
        inp_date = input().split()
    else:
        inp_date = read_txt[lp0 + 1].split()
    # print("入力された比較: {}, 身長: {}".format(inp_date[0], inp_date[1]))
    # 身長が低いほう
    if inp_date[0] == "le":
        le_list.append(float(inp_date[1]))
    # 身長が高いほう
    elif inp_date[0] == "ge":
        ge_list.append(float(inp_date[1]))
    else:
        print("比較データが不正です")

print("{} {}".format(max(ge_list), min(le_list)))