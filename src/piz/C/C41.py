# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = "2017/12/07"

# テキストからの読み込み
txt_list = []
try:
    with open("C41","r",encoding="utf-8") as inp_txt:
        txt_list = [txt for txt in inp_txt]
        # print("入力されたテキストは: {}".format(txt_list))
        inp_txt.close()
except:
    pass

medals_list =[]
lp_num = int(input()) if len(txt_list) == 0 else int(txt_list[0])
for lp0 in range(lp_num):
    if len(txt_list) == 0:
        medals = list(map(int, input().split()))
    else:
        medals = list(map(int, txt_list[lp0 + 1].split()))
    # print("入力されたメダルの数 金: {}, 銀: {}, 銅: {}".format(medals[0], medals[1], medals[2]))
    medals_list.append(medals)

# リストの要素を逆順でソートする
medals_list.sort(reverse=True)
for ans in medals_list:
    print(" ".join(list(map(str, ans))))