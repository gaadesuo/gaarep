# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2017 / 11 / 24


l_1 = list(input())
l_2 = list(input())

print("OK" if l_1[-1] == l_2[0] and l_2[-1] != "n" else "NG")