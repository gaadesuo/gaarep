# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/18 :09:38$'


def inp_func():
    """
    クローゼットにある服について、手前のものから順番にそれが夏物か冬物かの
    情報を表す 10 個の文字cが半角スペース区切りで与えられるのでリストにして返す
    c は英字大文字で "S", "W" のうちいずれか
    :return: list[str]
    """
    c_list = input().split()
    return c_list


def winter_change_func(c_list):
    """
    与えられたリストのうち5着以上が冬物になっているかどうか
    (なっていれば OK、なっていなければ NG) を返す
    :param c_list:10着の服の種類
    :return: 準備ができてるか否か
    """
    ans_word = "OK" if c_list.count("W") >= 5 else "NG"
    return ans_word


# ***処理***
inp_word_list = inp_func()
print("{}".format(winter_change_func(inp_word_list)))