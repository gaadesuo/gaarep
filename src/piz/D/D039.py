# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/16 :16:27$'


def inp_func():
    """
    入力された3つの数字を返す
    ・1 ≦ a ≦ 100
    ・1 ≦ b ≦ 100
    ・1 ≦ c ≦ 100
    :return: int 入力された3つの数字
    """
    a = int(input())
    b = int(input())
    c = int(input())
    return a, b, c


def equilateral_triangle_choise_func(a, b, c):
    """
    3つの数字がすべて正しいか判定する
    :param a: 入力された数字
    :param b: 入力された数字
    :param c: 入力された数字
    :return: str 正しいなら'YES'違うなら'NO'
    """
    ans_word = "YES" if a == b == c else "NO"
    return ans_word


# ***処理***
triangle_a, triangle_b, triangle_c = inp_func()
print("{}".format(equilateral_triangle_choise_func(
    triangle_a, triangle_b, triangle_c)))