# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/00/00 :00:00$'


def inp_func():
    """
    入力された文字列sと入力された数字nを返す
    1 ≦ 入力された文字列sの長さ ≦ 100
    1≦ n ≦ 文字列sの長さ
    :return: s, n
    """
    s = input()
    n = int(input())
    return s, n


def word_cut_func(s, n):
    """
    入力された文字列sをn番目まで返す
    :param s: str 入力された文字列
    :param n: int 入力された数字
    :return: str カット後の文字列
    """
    cut_word = s[0: n]
    return cut_word


# ***処理***
inp_word, inp_num = inp_func()
print("{}".format(word_cut_func(inp_word, inp_num)))