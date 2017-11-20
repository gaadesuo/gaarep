# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/20 :07:26$'


def inp_func():
    """
    入力された数値cを返す
    0 ≦ c ≦ 100
    :return: int 入力された数値
    """
    c = int(input())
    return c


def return_shocolate_func(c):
    """
    らったチョコレートが 1 つ以上であればその 3 倍の数を
    0 個であれば自分用に 1 つ用意するのでその値を返す
    :param c: int もらったチョコレートの数
    :return: 用意するチョコレートの数
    """
    chocolate = c * 3 if c > 0 else 1
    return chocolate


# ***処理***
inp_num = inp_func()
print("{:0d}".format(return_shocolate_func(inp_num)))