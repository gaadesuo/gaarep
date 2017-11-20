# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/20 :08:43$'


def inpu_func():
    """
    文字列sが入力されるので返す
    ・s は半角英数字で構成された文字列
    ・1 ≦ 文字列 s の長さ ≦ 100
    :return: str 入力された文字列
    """
    s = input()
    return s


def change_false(s):
    """
    入力された文字列にFalseが含まれるなら、含まれる「False」を「True」に置き換えて返す
    含まれない場合はそのまま返す
    :param s: str 入力された文字列
    :return: str 処理後の文字列
    """
    ans = s.replace("False", "True")
    return ans


# ***処理***
inp_word = inpu_func()
print("{}".format(change_false(inp_word)))