# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/18 :09:17$'


def inp_func():
    """
    子供 1、子供 2 が要求するお月見だんごの数を表す整数 d_1, d_2 が
    半角スペース区切りで与えられるのでこれをリストにして返す
    1 ≦ d_1, d_2 ≦ 1,000
    :return: list[int]
    """
    d_list = [int(d) for d in input().split()]
    return d_list


def dangohasine_func(d_list):
    """
    与えられたリストの要素の値が5以上の時は5に変換したリストにしてそれの合算値を返す
    :param d_list: 団子の要求数
    :return: 与える団子の数
    """
    dango_list = [5 if give_num >= 5 else give_num for give_num in d_list]
    dango_num = sum(dango_list)
    return dango_num


# ***処理***
inp_num_list = inp_func()
print("{:0d}".format(dangohasine_func(inp_num_list)))