# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/18 :11:06$'


def inp_func():
    """
    作りたいピラミッドの段数を表す整数nが与えられるのでそれを返す
    1 ≦ n ≦ 100
    :return: int 入力された数
    """
    n = int(input())
    return n


def humens_num_func(n):
    """
    入力されたn段のピラミッド必要な人数を計算して返す
    :param n: ピラミッドの段数
    :return: int 必要人数
    """
    humens_num = 0
    for necessary in range(1, n + 1):
        humens_num += necessary
    return humens_num


# ***処理***
inp_num = inp_func()
print("{:0d}".format(humens_num_func(inp_num)))