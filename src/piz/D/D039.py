# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/04'


txt_list = []
paiza = 0

try:
    with open("D039", "r",encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたデータは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

num_list = []
if paiza == 1:
    for lp0 in range(3):
        num_list.append(int(input()))
else:
    num_list = [int(num) for num in txt_list]
# print("入力された三辺の長さは【{}】です".format(num_list))
print("YES" if num_list[0] == num_list[1] == num_list[2] else "NO")