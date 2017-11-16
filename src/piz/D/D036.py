# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/14 :16:10$'


def inp_func():
    """
    入力された文字列sを返す
    ・s は半角小文字アルファベットで構成された文字列
    ・1 ≦ 文字列 s の長さ ≦ 100
    :return: int s
    """
    s = input()
    return s


def change_at_func(s):
    """
    入力された文字列から'at'っを探し@と置き換える
    :param s: 入力された文字列
    :return: 変更した文字列
    """
    split_word = s.split("at")
    return split_word


# ***処理***
inp_word = inp_func()
print("@".join(change_at_func(inp_word)))