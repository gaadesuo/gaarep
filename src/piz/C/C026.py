#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/06 15:15'

import numpy as np
# 入力
date_list = []
carrot_list = []
t_list = []

try:
    with open("C026", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt.strip())
        inp_txt.close()
    date_list = [int(i) for i in t_list.pop(0).split()]
    for l in t_list:
        num_list = [int(i) for i in l.split()]
        carrot_list.append(num_list)

except FileNotFoundError:
    date_list = [int(i) for i in input().split()]
    for i in range(date_list[0]):
        num_list = [int(i) for i in input().split()]
        carrot_list.append(num_list)

# print("本数: 糖度: ±: {}".format(date_list))
# print("人参のデータリスト: {}".format(carrot_list))

# 処理
big_list = []
np_carrot = np.array(carrot_list)
# print(np_carrot[:, -1])
np_t = np.where((date_list[1] - date_list[2] <= np_carrot[:, -1]) & (date_list[1] + date_list[2] >= np_carrot[:, -1]))
# print("糖度内の人参のインデックス: {}".format(np_t[0]))
if len(np_t[0]) == 0:
    print("not found")
elif len(np_t[0]) == 1:
    print(np_t[0][0] + 1)
else:
    for i in np_t[0]:
        # 糖度内の大きさを比較
        big_list.append(carrot_list[i][0])
    index_num = big_list.index((max(big_list)))
    # print("糖度内の最大の大きさのインデックス番号: {}".format(index_num))
    # 糖度内の人参インデックスリストからインデックス参照で糖度内の最大を表示　＋１で順番
    print(np_t[0][index_num] + 1)