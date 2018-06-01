# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/24$'

txt_list = []
paiza = 0

try:
    with open("D043", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたデータは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

inp_num = int(input()) if paiza == 1 else int(txt_list[0])
print("sunny" if inp_num <= 30 else "rainy" if inp_num >= 71 else "cloudy")