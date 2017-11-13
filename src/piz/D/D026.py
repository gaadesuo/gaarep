# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/13 :16:10$'


def inp_func():
    """
    入力した文字dをリストに入れて返す
    dは「yes」か「no」の文字列
    :return: 入力された文字列のリスト
    """
    d_list = [input() for lp0 in range(7)]
    return d_list


def no_count_func(d_list):
    """
    文字列'no'をカウントしてその数字を返す
    :param d_list: 入力された文字列のリスト
    :return: 'no'をカウントした数字
    """
    count_num = d_list.count("no")
    return count_num


# ***処理***
inp_word = inp_func()
print("{:0d}".format(no_count_func(inp_word)))