# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2017 / 12 / 22


txt_list = []
try:
    with open("C029", "r", encoding="utf-8") as inp_txt:
        txt_date = [txt.strip() for txt in inp_txt]
        txt_list.append(txt_date)
        # print("入力されたテキストデータは: {}".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    pass

rainy_list = []
if len(txt_list) == 0:
    day_date = list(map(int, input().split()))
    for lp0 in range(day_date[0]):
        rainy_date = list(map(int, input().split()))
        rainy_list.append(rainy_date)
else:
    day_date = list(map(int, txt_list[0][0].split()))
    for rainy in txt_list[0][1:]:
        rainy_date = list(map(int, rainy.split()))
        rainy_list.append(rainy_date)

# print("旅行の日数は{}日、連休の降水確率のリストは{}".format(day_date[1], rainy_list))

rainy_num = 0
travel_rainy_list = []
# 連休の旅行に行ける最終日のインデックス番号
last_day = len(rainy_list) - (day_date[1])
for day in range(0, last_day + 1):
    for travel in range(day_date[1]):
        # 旅行に行く初日から旅行の期間の降水確率を取得しリストに入れる
        rainy_num += rainy_list[day + travel][1]
    travel_rainy_list.append(rainy_num)
    rainy_num = 0
# print("連休初日からの旅行期間の合計降水確率のリスト: {}".format(travel_rainy_list))

min_index = travel_rainy_list.index(min(travel_rainy_list))
ans = rainy_list[min_index][0]
print("{:0d} {:0d}".format(ans, ans + (day_date[1] - 1)))