#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/26 03:15'

import re


def pass_check(s):
    """
    8文字以上で大文字小文字数を含んだものかをチェック
    :param s: 入力された数字
    """
    big_check = re.compile(r"([A-Z])+")
    small_check = re.compile(r"[a-z]+")
    num_check = re.compile(r"[0-9]+")
    decision = big_check.search(s)
    if decision and small_check and num_check and len(s) > 7:
        print("ok")
    else:
        print("NG")


word = input()
pass_check(word)
