# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/16 :15:38$'

import numpy as np


def inp_func():
    """
    7降水確率nを7日分入力しリストにして返す
    0 ≦ n ≦ 100
    :return: 入力された数字のリスト
    """
    n_list = []
    for lp0 in range(7):
        n = int(input())
        n_list.append(n)
    return n_list


def outing_choise(n_list):
    """
    入力されたリストの数値で30以下の数値が何個あるかをカウントし返す
    :param n_list: 入力された数字のリスト
    :return: int 30以下の数字の個数
    """
    np_n_list = np.array(n_list)
    ans_num = len(np.where(np_n_list <= 30)[0])
    return ans_num


# ***処理***
rainy_date_list = inp_func()
print("{:0d}".format(outing_choise(rainy_date_list)))