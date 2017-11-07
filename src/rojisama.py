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

# 生贄 白い祈りの生贄

# -*- coding: utf-8 -*-
# ***データ入力***
inp_word = list(input())
# print("入力された文字は" + str(inp_word))

# ***処理***
ans_list = []
if inp_word[0] == "w": # 最初がwの時に0を入れる
    ans_list.append("0")
    color = inp_word[0] # colorは前回の色確認用。ここで初期の色を入れる
else:
    color = inp_word[0]
# print("一番最初の色は" +str(color))

black = 0
white = 0
for word in inp_word:
    if word == color:
        if word == "b":
            black += 1
        else:
            white += 1
    else:
        if word == "b":
            black += 1
            ans_list.append(str(white))
            white = 0
        else:
            white += 1
            ans_list.append(str(black))
            black = 0
    color = word # 今回の色情報を入れる

if black > 0: # 最後終わったとき最終の値をリストに入れる
    ans_list.append(str(black))
else:
    ans_list.append(str(white))

print(" ".join(ans_list))
