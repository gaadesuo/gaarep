# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/13 :18:54$'


def inp_func():
    """
    入力された数字nを返す
    ・0 ≦ n ≦ 100
    n は整数
    :return: int 入力された数字
    """
    n = int(input())
    return n


def buttery_math(n):
    """
    100から入力された数字を引いて残りのバッテリー容量を求めて返す
    :param n: int 入力された数字
    :return: int 残りのバッテリー数
    """
    remaining = 100 - n
    return remaining


# ***処理***
buttery_num = inp_func()
print("{:0d}".format(buttery_math(buttery_num)))