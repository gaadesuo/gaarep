# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/158 :16:03$'


def inp_func():
    """
    整数 L, M, N がこの順に半角スペース区切りで与えられるのでリストにして返す
    ・1 ≦ L, M, N ≦ 20
    :return: list[int]
    """
    num_list = [int(num) for num in input().split()]
    return num_list[0], num_list[1], num_list[2]


# ***処理***
a_1, b, a_2 = inp_func()
print("{}{}{}".format("A" * a_1, "B" * b, "A" * a_2))