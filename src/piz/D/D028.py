# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2018/03/22'

txt_list = []
paiza = 0

try:
    with open("D028", "r", encoding="utf-8" )as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        print("入力されたデータは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

