# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/09 :13:58$'


def inp_com():
    """
    数字の入力割られる数m割る数nを入力して返す
    1 ≦ m ≦ 100
    1 ≦ n ≦ 100
    :return: int 入力した数字
    """
    inp_num = [int(num) for num in input().split()]
    return inp_num[0], inp_num[1]


def math_com(m, n):
    """
    mをnで割った商と余りを返す
    :param m: int 割られる数
    :param n: int 割る数
    :return: int 商と余り
    """
    ans_syou = int(m / n)
    ans_amari = m % n
    return ans_syou, ans_amari


# ***処理***
waru, warare = inp_com()
syou, amari = math_com(waru, warare)
print("{:0d} {:0d}".format(syou, amari))