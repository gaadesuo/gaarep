# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/20 :09:04$'


def inp_fuinc():
    """
    入力された数字nを桁ごとにリストにし100の位だけ返す
    ・n は整数
    ・100 ≦ n ≦ 999
    :return: str 入力された数字の百の位の数字
    """
    inp_num_list = list(input())
    return inp_num_list[0]


def erroe_check(n):
    """
    百の位の数字が2 であれば ok、4 であれば error、以外全ての数字は unknownを返す
    :param n: int 百の位の数字
    :return: str 対応した文字列
    """
    ans_word = "ok" if n == "2" else "error" if n == "4" else "unknown"
    return ans_word


# ***処理***
inp_num_x00 = inp_fuinc()
print("{}".format(erroe_check(inp_num_x00)))