# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/13 :19:11$'


def inp_func():
    """
    入力された文字列sを空白で分けリストにして返す
    ・2 ≦ 文字列 sの長さ ≦ 20
    sは半角アルファベットで構成された文字列
    1文字目は必ず半角アルファベット大文字で入力されます。
    :return: 入力された文字列のリスト
    """
    s_list = input().split()
    return s_list


def initial_word_func(s_list):
    """
    入力された性と名から一文字だけを返す
    :param f_name: 性
    :param l_name: 名
    :return: 性名の頭文字
    """
    fast_name_list = list(name[0])
    last_name_list = list(name[1])
    f_initial = fast_name_list[0]
    l_initial = last_name_list[0]
    return f_initial, l_initial


# ***処理***
name = inp_func()
fast_name, last_name = initial_word_func(name)
print("{}.{}".format(fast_name, last_name))