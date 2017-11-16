# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/16 :11:11$'


def inp_func():
    """
    2次行列abcdが入力される
    abとcdは改行で入力され各々スペースで区切られている
    この数字を返す
    ・-1000 ≦ a ≦ 1000
    ・-1000 ≦ b ≦ 1000
    ・-1000 ≦ c ≦ 1000
    ・-1000 ≦ d ≦ 1000
    :return: int 入力された数字
    """
    inp_num_a_b = [int(num) for num in input().split()]
    inp_num_c_d = [int(num) for num in input().split()]
    return inp_num_a_b[0], inp_num_a_b[1], inp_num_c_d[0], inp_num_c_d[1]


def math_func(a, b, c, d):
    """
    入力された数字を計算して返す
    :param a: int 一次の行列の数字a
    :param b: int 一時の行列の数字b
    :param c: int 二次の行列の数字c
    :param d: int 二次の行列の数字d
    :return: int 計算結果
    """
    ans_num = (a * d) - (b * c)
    return ans_num


# ***処理***
num_a, num_b, num_c, num_d = inp_func()
print("{:0d}".format(math_func(num_a, num_b, num_c, num_d)))