# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/09 :11:00$'


def inp_com():
    """
    s は以下の半角英字大文字の中から1文字が与えられます。
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    入力された文字のアスキーコードを返す
    :return: int 入力された文字のアスキーコート
    """
    s_ascii = ord(input())
    return s_ascii


def str_num(s):
    """
    入力された文字sのアスキーコードからaのアスキーコードを引く
    :param s: int 入力された文字列のアスキーコード
    :return: a から何番目後かの数字
    """
    # aのアスキーコードを代入
    a_ascii_num = ord("a") - 1
    ans_num = s - a_ascii_num
    return ans_num


# ***処理***
ascii_num = inp_com()
print(str_num(ascii_num))