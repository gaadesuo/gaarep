# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = "2017/12/18"

txt_list = []
try:
    with open("C30", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for  txt in inp_txt]
        # print("入力されたテキストリストは: {}".format(txt_list))
        inp_txt.close()
except:
    pass

inp_list = []
if len(txt_list) == 0:
    count_num = list(map(int, input().split()))
    for lp0 in range(count_num[0]):
        num = list(map(int, input().split()))
        inp_list.append(num)
else:
    for index in range(1, int(txt_list[0][0]) + 1):
        num = list(map(int, txt_list[index].split()))
        inp_list.append(num)
print("入力されたデータは: {}".format(inp_list))