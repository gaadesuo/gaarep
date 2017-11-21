# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/20 :11:00$'


def inp_func():
    """
    ステージに挑戦するために必要なスタミナ m 現在のあなたのスタミナ n
    がスペース区切りで与えられるのでそれを返す
    ・m, n は整数
・1 ≦ m, n ≦ 20
    :return: int 入力したそれぞれの数
    """
    nums = [int(num) for num in input().split()]
    return nums[0], nums[1]


def math_func(m, n):
    """
    ステージに挑戦可能であれば挑戦した後のスタミナの数値
    挑戦が不可能な場合は "No" を返す
    :param m: int ステージに挑戦するためにスタミナ
    :param n: int あなたの現在のスタミナ
    :return: int or str 各々の結果
    """
    ans_num = n - m
    ans_word = ans_num if ans_num >= 0 else "No"
    return ans_word


# ***処理***
sterge_num, hp = inp_func()
print("{}".format(math_func(sterge_num, hp)))