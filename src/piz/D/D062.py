# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/20 :07:35$'


def inp_func():
    """
    ひな壇の 1 段目、2 段目、3 段目に並べる人形の数を表す整数
    h_1, h_2, h_3 がこの順に半角スペース区切りで与えられるので
    リストにして返す
    ・1 ≦ h_1, h_2, h_3 ≦ 10
    ・h_1 + h_2 + h_3 = 10
    :return: int 入力された数値
    """
    h_list = [int(h) for h in input().split()]
    return h_list[0], h_list[1], h_list[2]


def row_doll_func(h_1, h_2, h_3):
    """
    各段にならべる人形の記号を返す
    人形は必ずもとの A, B, C, ... の順番で並べます
    :param h_1: int 一段目の人形の数
    :param h_2: int 二段目の人形の数
    :param h_3: int 三段目の人形の数
    :return: str 人形の順番
    """
    word = "ABCDEFGHIJ"
    fast = word[0:h_1]
    secound = word[h_1:h_1 + h_2]
    third = word[h_1 + h_2:]
    return fast, secound, third


# ***処理***
fast_num, second_num, third_num = inp_func()
# print("格段の並べる数値" + str(fast_num, second_num, third_num))
fast_row, second_row, third_row = row_doll_func(fast_num, second_num, third_num)
print(fast_row)
print(second_row)
print(third_row)