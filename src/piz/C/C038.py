# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = "2017/12/12"

import  numpy as np

txt_list = []
try:
    with open("C38", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたテキストは: {}".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    pass

if len(txt_list) == 0:
    inp_date = list(map(int, input().split()))
    date_list = [int(input()) for lp0 in range(inp_date[0])]
else:
    inp_date = list(map(int, txt_list[0].split()))
    date_list = [int(num) for num in txt_list[1:]]
# print("機械の数は: {}, お菓子の個数は: {}".format(inp_date[0], inp_date[1]))
# print("機械のお菓子を分ける個数のリスト: {}".format(date_list))
np_date_list = np.array(date_list)
amari_list = inp_date[1] % np_date_list
# print("リストの各々のあまりの数: {}".format(amari_list))
amari_min_index = np.where(amari_list==min(amari_list))
# print("最小の余りの機械のインデックスリスト: {}".format(amari_min_index))
if len(amari_min_index[0]) == 1:
    print((amari_min_index[0][0]) + 1)
else:
    ans_list = []
    for index in amari_min_index[0]:
        ans_list.append(date_list[index])
    # print("余り最小の機械のリスト: {}".format(ans_list))
    max_num = max(ans_list)
    print(date_list.index(max_num) + 1)