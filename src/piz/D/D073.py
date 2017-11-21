# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2017 / 11 / 21


"""
アルファベット大文字で構成された文字列 S が入力されるので
文字列を反転させて出力してください。
・1 ≦ 文字列 S の長さ ≦ 100
"""

inp_word = input()

# 反転させる
inp_word = inp_word[::-1]

print("{}".format(inp_word))