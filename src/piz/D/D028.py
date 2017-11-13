# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/13 :17:19$'


def inp_func():
    """
    入力された数列nを文字としてひとつづつリストに入れて返す
    ・1 ≦ n ≦ 10000
    n は整数
    :return: 文字列のリスト
    """
    n_list = list(input())
    return n_list


def digit_num_func(n_list):
    """
    リストの要素数を数えて桁数として返す
    :param n_list: 入力された数字を桁ごとに分けたリスト
    :return: int 桁数
    """
    n_digit = len(n_list)
    return n_digit


# ***処理***
inp_num_list = inp_func()
print("{:0d}".format(digit_num_func(inp_num_list)))