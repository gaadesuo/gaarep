# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/18 :08:04$'


def inp_func():
    """
    1 行目に金メダルの獲得者の名前を表す文字列 n_g が与えられます。
    2 行目に銀メダルの獲得者の名前を表す文字列 n_s が与えられます。
    3 行目に銅メダルの獲得者の名前を表す文字列 n_b が与えられます。
    入力された文字列nをリストにして返す
    :return: 入力された文字列のリスト
    """
    n_list = []
    for lp0 in range(3):
        n = input()
        n_list.append(n)
    return n_list


def medals_func(n_list):
    """
    入力された名前のリストとメダルリストの要素を共に[0]からタプルでまとめたリスト
    にしてそれを返す
    :param n_list: 入力された文字列のリスト
    :return: 名前とメダルをタプルでまとめたリスト
    """
    medals_list = ["Gold", "Silver", "Bronze"]
    ans_taple_list = zip(medals_list, n_list)
    return ans_taple_list


# ***処理***
inp_name_list = inp_func()
for medal_name in medals_func(inp_name_list):
    print("{} {}".format(medal_name[0], medal_name[1]))
