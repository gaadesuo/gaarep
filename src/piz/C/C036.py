# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = "2017/12/14"

txt_list = []
try:
    with open("C36", "r", encoding="utf-8") as txt_date:
        txt_list = [word.strip() for word in txt_date]
        # print("入力されたテキストデータのリストは{}".format(txt_list))
    txt_date.close()

except FileNotFoundError:
    pass

if len(txt_list) == 0:
    fast_vs = list(map(int, input().split()))
    second_vs = list(map(int, input().split()))
    fast_time = list(map(int, input().split()))
    second_time = list(map(int, input().split()))
else:
    fast_vs = list(map(int, txt_list[0].split()))
    second_vs = list(map(int, txt_list[1].split()))
    fast_time = list(map(int, txt_list[2].split()))
    second_time = list(map(int, txt_list[3].split()))
# print("一回戦第一試合: {}, 第二試合: {}".format(fast_vs, second_vs))
# print("一回戦タイム 1: {}, 2: {}, 3: {}, 4: {}".format(fast_time[0], fast_time[1],fast_time[2],fast_time[3]))

# 1回戦勝負
fast_win = fast_vs[0] if fast_time[fast_vs[0] - 1] < fast_time[fast_vs[1] - 1] else fast_vs[1]
sec_win = second_vs[0] if fast_time[second_vs[0] - 1] < fast_time[second_vs[1] - 1] else second_vs[1]
# print("1回戦勝者{} と{}".format(fast_win, sec_win))
final_vs = [fast_win, sec_win]
final_vs.sort()
if second_time[0] < second_time[1]:
    print(final_vs[0])
    print(final_vs[1])
else:
    print(final_vs[1])
    print(final_vs[0])