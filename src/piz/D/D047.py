#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/29 08:50'

# 入力
w_list = []
try:
    with open("D047", "r", encoding="UTF-8") as inp_txt:
        w_list = [i.strip() for i in inp_txt]
        inp_txt.close()

except FileNotFoundError:
    w_list = [input() for i in range(3)]

# print(w_list)

# 処理
print("""Gold {}
Silver {}
Bronze {}
""".format(w_list[0], w_list[1], w_list[2]))