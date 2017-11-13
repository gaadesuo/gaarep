# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/13 :15:41$'


def inp_func():
    """
    入力された数字nを返す
    ・1 ≦ n ≦ 100
    n は整数
    :return: int 入力された数字
    """
    n = int(input())
    return n


# ***処理***
inp_num = inp_func()
print("{:03d}".format(inp_num))