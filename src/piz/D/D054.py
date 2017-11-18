# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/18 :15:05$'


def inp_func():
    """
    入力された文字列sを返す
    s は数字 "1" で構成される文字列
    1 ≦ (s の長さ) ≦ 20
    :return: str
    """
    s = input()
    return s


def count_func(s):
    """
    1が11以上であれば"OK"、なければ足りない数を返す
    :param s: 入力された文字1の列
    :return: str or int ’OK'もしくは足りない数
    """
    ans = "OK" if len(s) > 10 else 11 - len(s)
    return ans


# ***処理***
inp_1 = inp_func()
print("{}".format(count_func(inp_1)))
