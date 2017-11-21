# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2017 / 11 / 21


"""
時刻のうち n 時の部分が日をまたいで 25 時となってしまった場合は 1 時とするように
0 時から 23 時までの 24 時間表記として正しい数値に修正するプログラムを作成してください。
・n は整数
・0 ≦ n ≦ 47
"""

inp_num = int(input())
# 24以上の時は24を引く
ans_num = inp_num - 24 if inp_num > 23 else inp_num

print("{:0d}".format(ans_num))