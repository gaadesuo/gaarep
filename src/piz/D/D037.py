# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2018/04/04'

import math

txt_list = []
paiza = 0

try:
    with open("D037", "r" , encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたデータは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

if paiza == 1:
    use = int(input())
    day = int(input())
else:
    use = int(txt_list[0])
    day = int(txt_list[1])

# print("ティッシュを使うまでの日にちは【{}】日、残りの花粉の日は【{}】です".format(use, day))
print(math.ceil(day / use))
