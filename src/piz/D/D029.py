# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/13 :17:39$'


def inp_func():
    """
    入力された数字nを返す
    ・1 ≦ n ≦ 6
    n は整数
    :return: int 入力された数字
    """
    n = int(input())
    return n


def math_func(n):
    """
    7から入力された数字を引いてさいころの裏面の数字を求める
    :param n: int 入力された数字
    :return: サイコロの裏面の数字
    """
    ans_num = 7 - n
    return ans_num


# ***処理***
dice_num = inp_func()
print("{:0d}".format(math_func(dice_num)))