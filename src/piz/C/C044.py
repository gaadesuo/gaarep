# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = "2017/12/07"
import collections

txt_list = []
try:
    with open("C44","r",encoding="utf-8") as inp_txt:
        txt_list = [word.strip() for word in inp_txt]
        # print("入力したテキストは: {}".format(txt_list))
        inp_txt.close()
except:
    pass

hand_list = []
lp_num = int(input()) if len(txt_list) == 0 else int(txt_list[0])
for lp0 in range(lp_num):
    if len(txt_list) == 0:
        hand = input()
    else:
        hand = txt_list[lp0 + 1]
    hand_list.append(hand)
# print("入力されたじゃんけんの手のリスト: {}".format(hand_list))
hand_dick = collections.Counter(hand_list)
# print("辞書化したあと: {}".format(hand_dick))
if len(hand_dick) == 3 or len(hand_dick) == 1:
    print("draw")
elif  "rock" in hand_dick.keys() and "scissors" in hand_dick.keys():
    print("rock")
elif "scissors" in hand_dick.keys() and "paper" in hand_dick.keys():
    print("scissors")
else:
    print("paper")