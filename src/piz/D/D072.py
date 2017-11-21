# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2017 / 11 / 21

import math

"""
バックアップをしたいデータの容量 X GBと外部記憶装置 1 つあたりの容量 Y GBと
外部記憶装置 1 つあたりの価格 P 円がスペース区切りで入力されます。
全てのデータをバックアップするために何円必要か計算するプログラムを作成してください。
・1 ≦ X ≦ 1000
・1 ≦ Y ≦ 1000
・1 ≦ P ≦ 10000
・X, Y, P は整数
"""

inp_date =[int(date) for date in input().split()]
print("保存したい容量[0], HDDの容量[1], 単価[2]" + str(inp_date))

# HDDの必要個数を繰り上げで求め単価を掛ける
price = math.ceil(inp_date[0] / inp_date[1]) * inp_date[2]

print("{:0d}".format(price))
