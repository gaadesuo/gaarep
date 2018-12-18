#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/11 22:16'

# 入力
call_list = []

try:
    with open("C033", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            call_list.append(txt.strip())
        inp_txt.close()
        del call_list[0]

except FileNotFoundError:
    for i in range(int(input())):
        call_list.append(input())

# print("コールリスト: {}".format(call_list))

# 処理
ball = 0
strike = 0

for s in call_list:
    if s == "ball":
        ball += 1
        print("fourball!" if ball == 4 else s + "!")
    elif s == "strike":
        strike += 1
        print("out!" if strike == 3 else s + "!")
