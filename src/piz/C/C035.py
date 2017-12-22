# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = "2017/12/15"

txt_list = []
try:
    with open("C35","r",encoding="utf-8") as inp_txt:
        txt_list = [word.strip() for word in inp_txt]
        # print("入力されたテキストは: {}".format(txt_list))
        inp_txt.close()
except:
    pass

point_list = []
if len(txt_list) == 0:
    for lp0 in range(int(input())):
        point = input().split()
        point_list.append(point)
else:
    for index in range(1, int( txt_list[0])):
        point = txt_list[index].split()
        point_list.append(point)
# print("受験者の学科と得点リスト: {}".format(point_list))
ans = 0
for men_date in point_list:
    # 学科判定の最初の一文字を取り出し別に格納、残りは数値化する
    department = men_date.pop(0)
    int_point = list(map(int, men_date))
    # print("学科: {}, 得点: {}".format(department, int_point))
    if sum(int_point) >= 350:
        if (department == "l" and (int_point[3] + int_point[4]) >= 160
            ) or (department == "s" and (int_point[1] + int_point[2]) >= 160):
            ans += 1

print(ans)
