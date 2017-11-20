# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/18 :20:27$'


def inp_func():
    """
    占い結果のトランプカードの 1 枚目、2 枚目に書かれた文字を表す
    c1, c2 がこの順に半角スペース区切りで与えられるのでそれを返す
    ・c1, c2 は "J", "Q", "K" のいずれか
    :return: list[str]
    """
    c_list = input().split()
    return c_list[0], c_list[1]


def card_change_func(c_1, c_2):
    """
     c1, c2 がともに "J" であったときのみ c_2 は "Q" に変更する
    :param c_1: str 一枚目のカードの中身
    :param c_2: str 二枚目のカードの中身
    :return: str カード二枚の中身
    """
    if c_1 == "J" and c_2 == "J":
        c_2 = "Q"
    return c_1, c_2


# ***処理***
fast_card, second_card = inp_func()
after_1, after_2 = card_change_func(fast_card, second_card)
print("{} {}".format(after_1, after_2))