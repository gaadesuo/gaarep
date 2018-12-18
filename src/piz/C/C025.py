#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/06 14:17'

# 入力
max_have = 0
fax_list = []
t_list = []

try:
    with open("C025", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt)
        inp_txt.close()
    max_have = int(t_list.pop(0))
    for l in t_list[1:]:
        n_list = [int(i) for i in l.split()]
        fax_list.append(n_list)

except FileNotFoundError:
    max_have = int(input())
    for i in range(int(input())):
        n_list = [int(i)for i in input().split()]
        fax_list.append(n_list)

# print("最大所持数: {}".format(max_have))
# print("faxのデータリスト: {}".format(fax_list))

# 処理
hour_fax = 0
hour_num = 0
ans_num = 0
total = lambda x, y: -(-x // y)

for l in fax_list:
    # print(hour_num, l, hour_fax)
    if hour_num == l[0]:
        hour_fax += l[2]
    else:
        hour_num = l[0]
        ans_num += total(hour_fax, max_have)
        hour_fax = l[2]
ans_num += total(hour_fax, max_have)

print(ans_num)