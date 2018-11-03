# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/03 18:58'

l = [1, 7, 3, 5]

for i in range(0, len(l) - 1):
    if l[i] > l[i + 1]:
        l.insert(i, l[i + 1])
        del l[i + 2]
print(l)
