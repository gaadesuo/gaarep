# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/11 :17:20$'


def inp_func():
    """
    入力された２つの角の数字a, bを返す
    :return: int 入力された２つの数字
    """
    a = int(input())
    b = int(input())
    return a, b


def angle_math(a, b):
    """
    三角形の内角のうち2つの角度が与えられるので残りの一つを計算し返す
    :param a: int 内角一つ
    :param b: int 内角一つ
    :return: int 残りの角の角度
    """
    ans_num = 180 - (a + b)
    return ans_num


# ***処理***
angle_a, angle_b = inp_func()
print("{:0d}".format(angle_math(angle_a, angle_b)))
