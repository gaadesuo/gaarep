# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/00/00 :00:00$'


def inp_func():
    """
    入力された文字列sを返す
    1 ≦ 文字数 ≦ 100
    s は半角アルファベットの小文字のみで構成されています。
    :return: 入力された文字列
    """
    inp_word = input()
    return inp_word


def change_func(s):
    """
    小文字の英語を大文字に変換する
    :param s: 入力された文字列
    :return: 変更した文字列
    """
    chang_word = s.upper()
    return chang_word


# ***処理***
word_list = inp_func()
print("{}".format(change_func(word_list)))