#! /usr/bin/python#
# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "user"
__date__ = "$2017/02/21 18:21:41$"

list = []
list2 = []

for nums in range(2,101):
    for num in range(2,nums - 1):
        if nums == num:
            pass
        else:
            if nums % num == 0:
                list.append(nums)

for nums2 in range(1,101):
    list2.append(nums2)

ans = set(list2) - set(list)
print(ans)
