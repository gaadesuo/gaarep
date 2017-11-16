# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/16 :10:39$'


def inp_func():
    """
    入力された数字nを返す
    2 ≦ n ≦ 100
    :return: int 入力された数字
    """
    n = int(input())
    return n


def math_func(n):
    """
    入力された数字を計算し答えを返す
    :param n: 入力された数字
    :return: int 対戦数
    """
    ans_num = int(((n ** 2) - n) / 2)
    return ans_num


# ***処理***
inp_num = inp_func()
print("{:0d}".format(math_func(inp_num)))