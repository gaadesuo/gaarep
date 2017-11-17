# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/16 :17:09$'


def inp_func():
    """
    入力された数字nを返す
    :return: int 入力された数字
    """
    n = int(input())
    return n


def weather_fonc(n):
    """
    入力された数字が
    ・0 % 以上 30 % 以下ならば "sunny"
    ・31 % 以上 70 % 以下ならば "cloudy"
    ・71 % 以上ならば "rainy"
    を返す
    :param n: int 入力された数字
    :return: str 結果
    """
    ans_word = "sunny" if n <= 30 else "rainy" if n >= 71 else "cloudy"
    return ans_word


# *** 処理***
rainy_num = inp_func()
print("{}".format(weather_fonc(rainy_num)))