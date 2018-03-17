# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2018/03/17$'

txt_list = []
paiza = 0
try:
    with open("D003", "r", encoding="utf-8") as inp_txt:
        txt_list = [num.strip() for num in inp_txt]
        # print("入力されたデーターは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

inp_num = 0
if paiza == 1:
    inp_num = int(input())
else:
    for inp_date in txt_list:
        inp_num = int(inp_date)
# print("入力された数字は【{}】です".format(inp_num))
ans = [str(inp_num * mug) for mug in range(1, 10)]
print(" ".join(ans))
