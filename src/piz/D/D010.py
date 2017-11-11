# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/9 :10:20$'


def inp_func():
    """
    文字の入力ローカル部Sとドメイン部tが入力される
    1 ≦ 文字列 ≦ 64
    s , t は半角英数と「.」(半角ドット)で構成された文字列
    :return: str 入力された文字列を返す
    """
    s = input()
    t = input()
    return s, t


# ***処理***
local, domain = inp_func()
print("{}@{}".format(local, domain))