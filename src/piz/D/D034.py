# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/14 :10:01$'


def inp_conf():
    """
    入力された数字nを返す
    ・2 ≦ n ≦ 21
    n は整数
    :return: int 入力された数字
    """
    n = int(input())
    return n


def god_choise_conf(n):
    """
    21から入力された数字を割って余りの数字を返す
    あまりが0の時は入力された数字を返す
    :param n:
    :return: int あまりの数
    """
    ans_num = 21 % n
    if ans_num == 0:
        ans_num = n
    return ans_num


# ***処理***
inp_num = inp_conf()
print("{:0d}".format(god_choise_conf(inp_num)))
