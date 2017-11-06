# -*- coding: utf-8 -*-

# 召喚の書 翼

# ***データ入力***
inp_num = int(input())
inp_word = list(input())
# print("入力された数字は " + str(inp_num))
# print("入力された文字は " + str(inp_word))

# ***処理***
l_list = []
r_list = []
for num in range(inp_num):
    if inp_word[num] == "L":
        l_list.insert(0, str(num + 1))
        # print("左からの数字" + str(l_list))
    else:
        r_list.append(str(num + 1))
        # print("右からの数字" + str(r_list))
# リストをまとめる
ans_list = l_list + r_list

# ***表示***
print(" ".join(ans_list))