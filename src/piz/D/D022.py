# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/10 :17:37$'


def inp_func():
    """
    入力した数字aを返す
    1 ≦ a ≦ 20
    a は正の整数
    :return: 入力された数字
    """
    n = int(input())
    return n


def math_func(a):
    """
    一辺がaの長さの正立方体の表面積を求めて返す
    :param a: int 一辺の長さ
    :return: int 立方体の表面積
    """
    ans_num = 6 * (a ** 2)
    return ans_num


# ***処理***
side_num = inp_func()
print("{:0d}".format(math_func(side_num)))