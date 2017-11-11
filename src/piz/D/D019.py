# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/00/00 :00:00$'


def inp_func():
    """
    入力された文字列sと数字nをリストにして返す
    1 ≦ n ≦ 文字列sの長さ
    1 ≦ 文字列sの長さ ≦ 10
    :return: str 入力された文字列, int 数字
    """
    inp_list = input().split()
    return inp_list[0], int(inp_list[1])


def word_func(s, n):
    """
    文字列sのn番目の文字を返す
    :param s: str 入力された文字列
    :param n: int 抜き出す場所の数字
    :return: str 指定された文字
    """
    after = s[n - 1: n]
    return after


# ***処理***
word, num = inp_func()
print("{}".format(word_func(word, num)))