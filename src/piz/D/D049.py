# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/08/58 :08:59$'


def inp_func():
    """
    アンケートの回答を表す文字列 S が与えられ、それを返す
    S は英字小文字からなる文字列
    S に "noaki" という文字列は 2 つ以上含まれず、含まれる場合必ず末尾に含まれる。
    1 ≦ (S の長さ) ≦ 20
    :return: str 入力された文字列
    """
    s = input()
    return s


def noaki_cutter_func(s):
    """
    入力された文字列から'noaki'という文字列があるならそれを省いた文字列を返す
    :param s: str 入力された文字列
    :return: str 'noaki'があるならそれを省いた文字列
    """
    if s.find("noaki"):
        slit_word = s.split("noaki")
        return slit_word[0]
    else:
        return s


# ***処理***
inp_word = inp_func()
print("{}".format(noaki_cutter_func(inp_word)))