# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2017 / 11 / 21


"""
お酒飲み放題がある場合は 6000 円、お酒飲み放題がない場合は 4000円のお店において
お酒飲み放題をつける人数が n 人、お酒飲み放題をつけない人数が m 人
それぞれ与えられるので合計が何円かを出力してください。
"""

humen_num = [int(men) for men in input().split()]
price = (humen_num[0] * 6000) + (humen_num[1] * 4000)
print("{:0d}".format(price))