# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2017 / 11 / 21


"""
あなたの 7 科目それぞれの点数と合格点が与えられるので、合格する場合は"pass"を、
不合格の場合は"failure"を出力してください。
"""

inp_num_list = [int(num) for num in input().split()]
pass_num = int(input())
# 平均点を出す
ans_num = sum(inp_num_list) / 7


print("pass" if pass_num <= ans_num else "failure")