# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ =  "2017 / 12 / 06"

import collections

# テスト入力txtの読み込み
read_txt = []
try:
    with open("C43","r",encoding="utf-8") as inp_txt:
        read_txt = [txt for txt in inp_txt]
        print("入力されたテストtxtデータは: {}".format(read_txt))
        inp_txt.close()
except:
    pass

# テキスト入力がなければinput()入力
if len(read_txt) == 0:
    dummy = int(input())
    inp_list = list(map(int, input().split()))
else:
    dummy = int(read_txt[0][0])
    inp_list = list(map(int, read_txt[1].split()))
# print("入力された数字のリスト: {}".format(inp_list))
# 数字の種類をキーにそのカウントを値とした辞書を作る
num_dick = collections.Counter(inp_list)
# print("IDと使用回数を辞書化したもの: {}".format(num_dick))
max_val = max(num_dick.values())
# print("与えられた数字の最大カウント数は: {:0d}".format(max_val))
ans_list = [key for key, val in num_dick.items() if val == max_val]
ans_list.sort()
print(" ".join(list(map(str, ans_list))))
