# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = "2017/12/17"

txt_list = []
try:
    with open("C32", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたテキストリストは: {}".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    pass

date_list = []
if len(txt_list) == 0:
    for lp0 in range(int(input())):
        date = list(map(int, input().split()))
        date_list.append(date)
else:
    for lp0 in range(1,int(txt_list[0]) + 1):
        date = list(map(int, txt_list[lp0].split()))
        date_list.append(date)
# print("入力されたデータは: {}".format(date_list))

point5_0 = 0
point3_1 = 0
point2_2 = 0
point1_3 = 0

for buy_date in date_list:
    if buy_date[0] == 0:
        point5_0 += buy_date[1]
    elif buy_date[0] == 1:
        point3_1 += buy_date[1]
    elif buy_date[0] == 2:
        point2_2 += buy_date[1]
    elif buy_date[0] == 3:
        point1_3 += buy_date[1]
# print("購入データ 食料品: {}, 書籍: {}, 衣類: {}, その他: {}".format(point5_0, point3_1, point2_2, point1_3))
total = 0
total += int(point5_0 * 0.01) * 5
total += int(point3_1 * 0.01) * 3
total += int(point2_2 * 0.01) * 2
total += int(point1_3 * 0.01)
print(total)
