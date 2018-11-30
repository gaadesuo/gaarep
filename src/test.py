#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/30 15:06'

men = 0
id_list = []
t_list = []

try:
    with open("test", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            t_list.append(txt)
        inp_txt.close()
        # print(t_list)
        men = int(t_list[0])
        id_list = [int(i) for i in t_list[1].split()]

except FileNotFoundError:
    men = int(input())
    id_list = [int(i) for i in input().split()]
# print(id_list)


# 人数分の0リスト作成
ans_list = []
for i in range(men):
    ans_list.append(0)
# print(ans_list)


# 上司のIDと直属部下のID
for i in id_list:
    ans_list[i - 1] += 1

subordinate = {}

for i in range(men):
    index_num = [n + 2 for n, v in enumerate(id_list) if v == i]
    if len(index_num) > 0:
        subordinate[i] = index_num

# print("直属上司のID: 自分のID {}".format(subordinate))


# 辞書を逆順から調べ直属上司のリストへ入れる
temp_dic = subordinate.copy()
for i in range(men, 0, -1):
    if i in subordinate.keys():
        for k, v in subordinate.items():
            if i in v:
                # print(k, v, i)
                for add_num in subordinate[i]:
                    # print(add_num)
                    temp_dic[k].append(add_num)


# 上司IDが何人部下がいるかを表示するリストへ代入
for k, v in temp_dic.items():
    ans_list[k - 1] = len(v)

# 表示
for i in ans_list:
    print(i)
