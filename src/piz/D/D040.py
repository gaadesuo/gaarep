# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/07'


txt_list = []
paiza = 0

try:
    with open("D040", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたデータは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

inp_num_list = []
count = 0
if paiza == 1:
    for lp0 in range(7):
        inp_num_list.append(int(input()))
else:
    inp_num_list = [int(num) for num in txt_list]
# print("7日間の降水確率は【{}】です".format(inp_num_list))
for rainy in inp_num_list:
    if rainy <= 30:
        count += 1
print(count)