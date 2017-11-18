# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/18 :15:49$'


def inp_func():
    """
    1 行目に子どもの通知表の成績を表す整数 g が与えられます
    2 行目にプレゼント候補を表す文字列pが安価な順に3つ半角スペース区切りで与えられます
    ・1 ≦ g ≦ 3
    ・pは英小文字で構成される文字列
    ・1 ≦ (pの長さ) ≦ 20
    :return:入力された数字と文字列のリスト
    """
    g = int(input())
    p_list = input().split()
    return g, p_list


def present_choise_func(g, p_list):
    """
    成績に応じてプレゼントを決める
    1ならリストの上位1番目～以下スライド
    :param g: int 成績
    :param p_list: list[str] プレゼント0から順番で高価
    :return: str 成績に対応したプレゼント
    """
    present = p_list[g - 1]
    return present


# ***処理***
inp_num, inp_word_list = inp_func()
print("{}".format(present_choise_func(inp_num, inp_word_list)))