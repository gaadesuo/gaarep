# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/11 :17:12$'


def inp_func():
    """
    入力された文字列sを返す
    ・1 ≦ sの長さ ≦ 100
    s は半角アルファベットで構成された文字列
    :return: str 入力された文字列
    """
    s = input()
    return s


def word_count_func(s):
    """
    入力された文字列の中のAをカウントし返す
    :param s: 入力された文字列
    :return: int Aの数
    """
    count_num = s.count("A")
    return count_num


# ***処理***
inp_word = inp_func()
print("{:0d}".format(word_count_func(inp_word)))