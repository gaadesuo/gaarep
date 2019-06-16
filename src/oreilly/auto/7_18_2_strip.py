#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/26 04:00'

import re


def t_strip(s, p):
    if s == "":
        f_sp_check = re.compile(r"^\s")
        e_sp_check = re.compile(r"\s$")

        if f_sp_check.search(p) and e_sp_check.search(p):
            return p[1:-1]
        elif f_sp_check.search(p):
            return p[1:]
        elif e_sp_check.search(p):
            return p[:-1]
        else:
            return p
    else:
        f_w_check = re.compile(r"^s")
        e_w_check = re.compile(r"s$")
        if f_w_check.search(p) and e_w_check.search(p):
            return p[1:-1]
        elif f_w_check.search(p):
            return p[1:]
        elif e_w_check.search(p):
            return p[:-1]
        else:
            return p


word = input()
p_word = "abcdefg\n"
print(t_strip(word, p_word))