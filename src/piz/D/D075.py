# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2017 / 11 / 21


"""
4 枚のカードの情報が改行区切りで入力されるので、 1 から 5 のカードのうち
足りないカードの数字を出力してください。
・1 ≦ c_1, c_2, c_3, c_4 ≦ 5
・c_1, c_2, c_3, c_4 は互いに異なる整数で与えられます。
"""

num_list = [1, 2, 3, 4, 5]


for lp0 in range(4):
    # 入力した数字をリストから消していく
    num = int(input())
    num_list.remove(num)

print("{:0d}".format(num_list[0]))