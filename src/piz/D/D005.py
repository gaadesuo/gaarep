# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/08 :17:02$'


def inp_com():
    """
    数字の入力
    0 <= 入力の数字 <= 100
    初項、公差が与えられる
    :return: 入力された数字のリスト
    """
    num_list = [int(num) for num in input().split()]
    return num_list[0], num_list[1]


def math_com(n, m):
    """
    等差数列そ求める
    初期値nにm倍された数字を10回ぶん計算し文字列に変更したリストにして返す
    :param n: int 初項
    :param m: int 公差
    :return: 答えのリスト
    """
    ans_list = [n + num for num in range(0, m * 10, m)]
    return map(str, ans_list)


# ***処理***
syokou, kousa = inp_com()
print(" ".join(math_com(syokou, kousa)))
