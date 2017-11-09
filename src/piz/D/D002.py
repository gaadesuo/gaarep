# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/08 :07:40$'


def inp_com():
    """
    数字の入力
    1 <= num <= 1000
    :return: 入力された数字
    """
    inp_num = [int(num) for num in input().split()]
    return inp_num


def big_small(num1, num2):
    """
    num1とnum2の大きさを比べる
    大きいほうの数字を返す
    数字が同じ場合はeqを返す
    :param num1: int num[0]
    :param num2: int num[1]
    :return: 正解
    """
    if num1 == num2:
        return "eq"
    elif num1 > num2:
        return num1
    else:
        return num2


# ***処理***
num = inp_com()
print(big_small(num[0], num[1]))