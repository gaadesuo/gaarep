# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/08 :17:54$'


def inp_func():
    """
    数字Nを入力する
    1 ≦ N ≦ 100
    :return: int 入力された数字
    """
    inp_num = int(input())
    return inp_num


def math_func(n):
    """
    偶数か奇数かを処理する
    n が奇数なら"odd" 偶数なら"even" と半角英文字で出力
    :param N: int 判定する数値
    :return: str 結果
    """
    ans_word = "even" if n % 2 == 0 else "odd"
    return ans_word


# ***処理***
inp_num = inp_func()
print("{}".format(math_func(inp_num)))