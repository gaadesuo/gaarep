# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/13 :16:55$'


def inp_func():
    """
    入力された数字nを返す
    ・2 ≦ n ≦ 100
    n は整数
    :return: int 入力された数字
    """
    n = int(input())
    return n


def math_func(n):
    """
    1から入力されたnまでの総和を求めて返す
    :param n: 入力された数字
    :return: int nまでの総和
    """
    ans_num = 0
    for num in range(1, n + 1):
        ans_num += num
    return ans_num


# ***処理***
inp_num = inp_func()
print("{:0d}".format(math_func(inp_num)))