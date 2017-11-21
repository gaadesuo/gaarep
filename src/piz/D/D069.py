# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/21 :17:16$'


def inp_func():
    """
    それぞれの人が何点だったかを 表す 7 個の整数aが半角スペース区切りで与えられるので
    それをリストにして返す
    a は 0 から 100 までの整数
    :return: list[int]
    """
    a_list = [ int(a) for a in input().split()]
    return a_list


def point_round_func(a_list):
    """
    リストの平均を出してそれを返す
    :param a_list: 7人のテストの点数
    :return: int 7人の平均点
    """
    ans_num = sum(a_list) / 7
    return ans_num


# ***処理***
inp_num_list = inp_func()
print("{:.1f}".format(point_round_func(inp_num_list)))