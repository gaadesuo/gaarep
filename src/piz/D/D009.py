# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/08 :18:19$'


def inp_func():
    """
    入力された数字を返す
    1 ≦ a, b ≦ 2014
    a < b
    :return: 入力された数字
    """
    inp_num = [int(num) for num in input().split()]
    return inp_num[0], inp_num[1]


def math_func(a, b):
    """
    bからaを引いて年数の差を求める
    :param a: int 引く数
    :param b: int ひかれる数
    :return: int 結果
    """
    ans_num = b - a
    return ans_num


# ***処理***
num_a, num_b = inp_func()
print("{:0d}".format(math_func(num_a, num_b)))