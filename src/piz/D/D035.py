# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/14 :16:02$'


def inp_func():
    """
    入力された数字dをスペースで分割してリストにして返す
    d は整数
    実在の日付でない可能性もあります。
    :return: 入力された数字の文字列のリスト
    """
    d = input().split()
    return d


inp_day = inp_func()
print("/".join(inp_day))