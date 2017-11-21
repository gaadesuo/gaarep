# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2017 / 11 / 21


"""
2つの正の整数 a, b が入力されるので、a と bを掛け算した時 9,999 以下であれば
掛け算した結果を出力し、10,000 以上の場合は "NG" と出力するプログラムを作成してください。
"""

inp_num_list = [int(num) for num in input().split()]
ans_num = inp_num_list[0] * inp_num_list[1]

print(ans_num if ans_num <= 9999 else "NG")
