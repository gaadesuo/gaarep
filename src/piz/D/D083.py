# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2017 / 12 / 01


num_list = [int(num) for num in input().split()]
print("STAND" if sum(num_list) >= 16 else "HIT")