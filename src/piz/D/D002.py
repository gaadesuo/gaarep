# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2018/03/17'

txt_list = []
paiza = 0
try:
    with open("D002", "r", encoding="utf-8") as inp_txt:
        txt_list = [word.strip() for word in inp_txt]
        # print("入力されたデータは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

inp_num = []
if paiza == 1:
    inp_num = [int(num) for num in input().split()]
else:
    for inp_date in txt_list:
        inp_num = [int(num) for num in inp_date.split()]
# print("入力された数字は【{}】です".format(inp_num))
print(inp_num[0] if inp_num[0] > inp_num[1] else inp_num[1] if inp_num[0] < inp_num[1] else "eq" )