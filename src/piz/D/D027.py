# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2018/03/22'

txt_list = []
paiza = 0

try:
    with open("D027", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたデータは【{}】です".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    paiza = 1

ans = 0
inp_num = int(input()if paiza == 1 else int(txt_list[0]))
# print("入力された数字は【{}】です".format(inp_num))
for num in range(1, inp_num + 1):
    ans += num
print(ans)