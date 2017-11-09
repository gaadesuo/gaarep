# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/00/00 :00:00$'


def inp_com():
    """
    入力された数字nを返す
    -100 ≦ n ≦ 100
    n は整数
    :return: int 入力された数字
    """
    n = int(input())
    return n


def change_com(n):
    """
    負の数字の場合-1を掛けて絶対値にして返す
    :param n: int 入力された数字
    :return: int 絶対値
    """
    if n < 0:
        n *= -1
    return n


# ***処理***
inp_num = inp_com()
print("{:0d}".format(change_com(inp_num)))