# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/18 :08:42$'


def inp_func():
    """
    8 月の台風の上陸日を表す 5 つの整数dが昇順に改行区切りで与えられます
    これをリストにして返す
    :return: 入力された日数の数字のリスト
    """
    d_list = []
    for lp0 in range(5):
        d = int(input())
        d_list.append(d)
    return(d_list)


def gap_num_func(d_list):
    """
    与えられたリストの要素のインデックス間の数値の差を返す
    :param d_list: 日数の数値のリスト
    :return: 日数間の差のリスト
    """
    ans_num_list = []
    for lp1 in range(4):
        ans_num = d_list[lp1 + 1] - d_list[lp1]
        ans_num_list.append(ans_num)
    return ans_num_list


inp_num_list = inp_func()
for ans in gap_num_func(inp_num_list):
    print("{:0d}".format(ans))
