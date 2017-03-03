#! /usr/bin/python#
# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "user"
__date__ = "$2017/02/21 18:21:41$"

list = []

for nums in range(2,101):
    for num in range(2,nums):
        if nums == num:
            pass
        else:
            if nums % num == 0:
                list.append(nums)

ans = set(list)
print(ans)
