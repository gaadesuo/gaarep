# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/18 :15:24$'


def inp_func():
    """
    半角スペースで区切られた文字列s2つをリストに入れ返す
    sは英字で構成される文字列 (半角スペース等は含まない)
    1 ≦ (sの長さ) ≦ 20
    :return: str
    """
    s_list = input().split()
    return s_list


# ***処理***
inp_word_list = inp_func()
print("Best in {} {}".format(inp_word_list[0], inp_word_list[1]))
