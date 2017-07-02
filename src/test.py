# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/05/24 :07:36$'
num = input()
print(num[:1])
if num[:1] == "2":
    print("ok")
elif num[:1] == "4":
    print("error")
else:
    print("unkown")