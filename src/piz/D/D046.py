# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/18 :08:25$'


def inp_func():
    """
    3 つのタマゴそれぞれを孵化させるのに必要な歩行距離(km)を表す整数
    d_1, d_2, d_3 がここの順に半角スペース区切りで与えられるので半角スペースで
    リスト化して返す
    :return: スリットした数字のリスト
    """
    d_list = [int(d) for d in input().split()]
    return d_list


def max_func(d_list):
    """
    与えられたリストの数値の最大値を返す
    :param d_list: 数値のリスト
    :return: int 数値のリストの最大値
    """
    max_num = max(d_list)
    return max_num


# ***処理***
inp_num_list = inp_func()
print("{:0d}".format(max_func(inp_num_list)))