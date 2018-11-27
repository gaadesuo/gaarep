#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/25 05:58'

txt_list = []
paiza = 0

# ファイルからの入力
try:
    with open("D002", "r", encoding="UTF-8") as inp_txt:
        txt_list = [i.strip() for i in inp_txt]
        # print(txt_list)
        inp_txt.close()

except FileNotFoundError:
    paiza = 1

# 処理
if paiza == 1:
    num_list = [int(i) for i in input().split()]
else:
    num_list = [int(i) for i in txt_list[0].split()]
# print(num_list)
print("eq" if num_list[0] == num_list[1] else max(num_list))
