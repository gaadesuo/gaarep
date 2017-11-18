# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/18 :11:19$'


def inp_func():
    """
    入力された文字列sを返す
    s は英字小文字で構成される文字列
    1 ≦ (s の長さ) ≦ 20
    :return: str 入力された文字列
    """
    s = input()
    return s


def choise_func(s):
    """
    入力された文字列が"candy" か "chocolate" であれば "Thanks!"
    その他の場合は "No!"を返す
    :param s:
    :return: str 入力に対するリアクション
    """
    ans_word = "Thanks!" if s == "chocolate" or s == "candy" else "No!"
    return ans_word


inp_word = inp_func()
print("{}".format(choise_func(inp_word)))
