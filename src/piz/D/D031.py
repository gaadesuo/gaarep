# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/13 :17:51$'


def inp_func():
    """
    入力された数字nを返す
    ・1 ≦ n ≦ 100
    n は整数
    :return: int 入力された数字
    """
    n = int(input())
    return n


def min_sec_func(minuts):
    """
    入力された数字に60を掛けた答えを返す
    :param minuts: 入力された数字
    :return: 分から秒に変換された数字
    """
    second = 60 * minuts
    return second


# ***処理***
minuts_num = inp_func()
print("{:0d}".format(min_sec_func(minuts_num)))