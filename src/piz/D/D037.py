# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/00/00 :00:00$'

import math


def inp_func():
    """
    ティッシュ1箱が空になるまでの期間を m 日
    残りの花粉症の季節を n 日が改行区切りで入力される
    ・1 ≦ m ≦ 100
    ・1 ≦ n ≦ 100
    :return: int 入力された数字
    """
    m = int(input())
    n = int(input())
    return m, n


def box_math_func(m, n):
    """
    入力された日数nを使用する日数mで割って何箱必要か求める
    あまりが出た場合は繰り上げ
    :param m: int 一箱の使用日数
    :param n: int トータル日数
    :return: 必要箱数
    """
    ans_num = int(math.ceil(n / m))
    return ans_num


# ***処理***
used_day, total_day = inp_func()
print("{:0d}".format(box_math_func(used_day, total_day)))