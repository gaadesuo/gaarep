# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/17 :13:21$'


def inp_func():
    """
    入力された数字を返す
    ・1 ≦ n ≦ 5
    :return: int 入植された数字
    """
    n = int(input())
    return n


def report_func(n):
    """
    入力した数字に対応した文字を返す
    :param n: int 入力された数字
    :return: str 対応した文字
    """
    word_list = ["E", "D", "C", "B", "A"]
    ans_word = word_list[n - 1]
    return ans_word


# ***処理***
inp_num = inp_func()
print("{}".format(report_func(inp_num)))
