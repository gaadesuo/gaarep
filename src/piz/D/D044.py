# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/17 :12:41$'


def inp_func():
    """
    2 つの文字列 s1, s2 が半角スペース区切りで与えられます
    ・s1 は半角英字で構成された文字列
    ・1 ≦ s1の長さ ≦ 100
    ・s2 は "M" か "F" のいずれか
    :return: 入力された文字列のリスト
    """
    s_list = input().split()
    return s_list


def m_f_choise(s2):
    """
    s2がFならMs MならMrを返す
    :param s2:
    :return: str ’Ms’’Mr’を返す
    """
    ans_word = "Ms" if s2 == "F" else "Mr"
    return ans_word


inp_word_list = inp_func()
sex_word = m_f_choise(inp_word_list[1])
print("Hi, {}. {}".format(sex_word, inp_word_list[0]))
