# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/20 :11:56$'


def inp_func():
    """
    スイッチを押した回数 n が1行目に与えられるので返す
    ・n は整数
    ・1 ≦ n ≦ 100
    :return: int 入力された回数
    """
    n = int(input())
    return n


def switch_change(n):
    """
     "OFF"状態からスイッチを押すとON OFFを繰り返す
     スイッチを押した回数 n が入力されるのでn 回スイッチが押された後の
     状態を "ON" か "OFF" の文字列で返す
    :param n: int スイッチを押した回数
    :return: str 最後の状態
    """
    ans_num = n % 2
    ans_word = "ON" if ans_num == 1 else "OFF"
    return ans_word


# ***処理***
inp_num = inp_func()
print("{}".format(switch_change(inp_num)))