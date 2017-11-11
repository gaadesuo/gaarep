# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/11 :17:04$'


def inp_func():
    """
    ２つの文字列sとtを入力して返す
    ・1 ≦ sの文字数 ≦ 10
    ・1 ≦ tの文字数 ≦ 10

    s と t は半角英数字で構成された文字列です
    :return: str 入力された文字列
    """
    s = input()
    t = input()
    return s, t


def word_comp(s, t):
    """
    ２つの文字列sとtを比較し同じならYes、違うならNoを返す
    :param s: 入力された文字列
    :param t: 入力された文字列
    :return: 成否判定
    """
    ans_word = "Yes" if s == t else "No"
    return ans_word


# ***処理***
word_s, word_t = inp_func()
print("{}".format(word_comp(word_s, word_t)))