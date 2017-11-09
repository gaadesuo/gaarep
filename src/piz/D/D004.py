# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/00/00 :00:00$'


def inp_com():
    """
    入力された文字列をリストに入れて返す
    :return: 入力された文字列
    """
    str_list = []
    for lp0 in range(int(input())):
        s = input()
        str_list.append(s)
    return str_list


# ***処理***
print("Hello " + ",".join(inp_com()) + ".")
