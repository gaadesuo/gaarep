# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/20 :16:12$'


def inp_func():
    """
    文字列の長さ n が 1 行目に与えられます
    晴れの日を "S" 、雨の日を "R" で記録した長さ n の文字列 s が2行目に与えられます
    ・n は整数
    ・s は "S" と "R" で構成された長さ n の文字列
    ・1 ≦ n ≦ 100
    :return: int list[str]
    """
    n = int(input())
    s = list(input())
    return s


def weather_func(s):
    """
    晴れの日を "S" 雨の日を "R" とし晴れの日数と、雨の日数を返す
    :param s: str 晴れの日を "S" 、雨の日を "R" で記録した文字列
    :return: int Sの数 Rの数
    """
    s_num = s.count("S")
    r_num = s.count("R")
    return s_num, r_num


# ***処理***
inp_word = inp_func()
s_count, r_count = weather_func(inp_word)
print("{:0d} {:0d}".format(s_count, r_count))
