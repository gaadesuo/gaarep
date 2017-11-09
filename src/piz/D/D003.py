# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/08 :07:55$'


def inp_com():
    """
    数字の入力
    1 ≦ n ≦ 100
    :return: 入力された数字
    """
    n = int(input())
    return n


def mag(n):
    """
    1～9まで掛けたものを返す
    :param num: int 掛ける元の数字
    :return: 答え
    """
    ans_num = [n * mag_num for mag_num in range(1, 10)]
    # print(ans_num)
    return map(str, ans_num)


# ***処理***
inp_num = inp_com()
print(" ".join(mag(inp_num)))