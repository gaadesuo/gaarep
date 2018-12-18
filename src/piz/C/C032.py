#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/11 19:43'

# 入力
point_dic = {}
t_list = []
for i in range(4):
    point_dic[i] = 0

try:
    with open("C032", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt)
        inp_txt.close()
    for l in t_list[1:]:
        n_list = [int(i) for i in l.split()]
        point_dic[n_list[0]] += n_list[1]

except FileNotFoundError:
    for i in range(int(input())):
        n_list = [int(i) for i in input().split()]
        point_dic[n_list[0]] += n_list[1]

# print("商品NO: 購入総額 {}".format(point_dic))

# 処理
total_point = 0
mag = [0.05, 0.03, 0.02, 0.01]

for i in range(4):
    total_point += int(int(point_dic[i] / 100) * 100 * mag[i])

print(total_point)