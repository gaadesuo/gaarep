# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/00/00 :00:00$'


def inp_func():
    """
    入力された5つの数字nをリストにして返す
    1 ≦n ≦ 99
    nは整数である
    return: 入力された数字のリスト
    """
    n_list = []
    for lp0 in range(5):
        n = int(input())
        n_list.append(n)
    return n_list


def max_min_func(n_list):
    """
    入力された数字のリストの最大値と最小値を求めて表示する
    :param n_list: 入力された数字のリスト
    :return: int 最大値, 最小値
    """
    ans_list = []
    ans_list.append(max(n_list))
    ans_list.append(min(n_list))
    for num in ans_list:
        print(num)


# ***処理***
inp_num_list = inp_func()
max_min_func(inp_num_list)