# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/10 :06:00$'


def inp_func():
    """
    入力した数字nを返す
    1 ≦ n ≦ 100
    :return: int 入力された数字
    """
    n = int(input())
    return n


def count_down_func(n):
    """
    入力された数字から１づつカウントダウンさせ１までの数字を表示する
    :param n: int カウントダウンが始まる数字
    :return: int カウントダウンしていってる数字
    """
    for num in range(n, 0, -1):
        print("{:0d}".format(num))


# ***処理***
inp_num = inp_func()
count_down_func(inp_num)