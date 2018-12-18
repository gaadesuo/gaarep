#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/05 08:43'

# 入力
make_num = 0
make_dic = {}
have_num = 0
have_dic = {}
t_list = []

try:
    with open("C018", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt)
        inp_txt.close()
        for i in range(int(t_list.pop(0))):
            k, v = t_list.pop(0).split()
            make_dic[k.strip()] = int(v)
        for i in range(int(t_list.pop(0))):
            k, v = t_list.pop(0).split()
            have_dic[k.strip()] = int(v)

except FileNotFoundError:
    for i in range(int(input())):
        k, v = input().split()
        make_dic[k] = int(v)
    for i in range(int(input())):
        k,v = input().split()
        have_dic[k] = int(v)

# print("レシピの辞書 種類: 数 {}".format(make_dic))
# print("持っているものの辞書 種類: 数 {}".format(have_dic))

# 処理
ans_list =[]
for k, v in make_dic.items():
    if k in have_dic:
        n = int(have_dic[k] / make_dic[k])
        # print(n)
        ans_list.append(n)
    else:
        ans_list.append(0)

print(min(ans_list))
