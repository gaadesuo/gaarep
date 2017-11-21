# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2017 / 11 / 21


"""
禁止ワード W と判定する文字列 S が改行区切りで順に与えられるので S に W が含まれて
いる時は "NG" それ以外の場合は文字列 S をそのまま出力してください。
・S, W は半角アルファベットで構成された文字列
・1 ≦ 文字列 S, W の長さ ≦ 100
"""
ng_word = input()
inp_word = input()

# NGワードを含むときはNGを返す
ans_word = "NG" if ng_word in inp_word else inp_word

print("{}".format(ans_word))