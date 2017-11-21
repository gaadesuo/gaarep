# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2017 / 11 / 21


"""
全ての文字が同じならNGを返し違うならOKを返す
・2 ≦ 文字列 S の長さ ≦ 100
・文字列 S は半角英数字で構成された文字列
"""

inp_word = list(input())
print(len(inp_word))
print(inp_word.count(inp_word[0]))
print("NG" if inp_word.count(inp_word[0]) == len(inp_word) else "OK")