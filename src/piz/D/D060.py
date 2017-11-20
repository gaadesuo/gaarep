# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/18 :21:25$'


def inp_func():
    """
    A, B のボタンを押した回数がAのボタン, Bのボタンの順に
    半角スペース区切りで与えられるのでそれを返す
    ・0 ≦ a, b ≦ 100
    :return: int 入力された数に2つ
    """
    push_list = [int(p) for p in input().split()]
    return push_list


def move_func(a, b):
    """
    A のボタンを押すとキャラクターが 1 マス右に進み (座標が 1 増える)
    B のボタンを押すとキャラクターが 1 マス左に進む (座標が 1 減る)
    ので最終座標を返す
    :param a: int Aボタンを押された回数
    :param b: int Bボタンを押された回数
    :return: int 最終座標
    """
    ans_num = a - b
    return ans_num


# ***処理***
a_push, b_push = inp_func()
print("{:0d}".format(move_func(a_push, b_push)))