# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ =  "2017 / 11 / 28"

txt_list = []
try:
    with open("C42","r",encoding="utf-8") as inp_txt:
        txt_list = [txt for txt in inp_txt]
        # print("テキストから入力されたデータは{}".format(txt_list))
        inp_txt.close()
except:
    pass

w_l_list = []
if len(txt_list) == 0:
    lp_num = int(input())
else:
    lp_num = int(txt_list[0])

for lp0 in range(lp_num):
    temp_list = list("-" * lp_num)
    w_l_list.append(temp_list)
# print("初期の対戦表は: {}".format(w_l_list))
for lp1 in range(int(((lp_num ** 2) - lp_num) / 2)):
    if len(txt_list) == 0:
        win_lose = list(map(int, input().split()))
    else:
        win_lose = list(map(int, txt_list[lp1 + 1].split()))
    # print("入力された 勝者: {}, 敗者: {}".format(win_lose[0], win_lose[1]))
    w_l_list[win_lose[0] -1][win_lose[1] - 1] = "W"
    w_l_list[win_lose[1] -1][win_lose[0] - 1] = "L"

for ans_list in w_l_list:
    print(" ".join(ans_list))