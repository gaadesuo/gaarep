# 休みと旅行のデータ入力[0]:連休 [1]:旅行の日
day = [int(lp0) for lp0 in input().split()]
# print("連休と旅行の日数" + str(day))

# 連休の日にちと降水確率のデータ入力
rain_list = []
for lp1 in range(day[0]):
    rain = [int(lp2) for lp2 in input().split()]
    rain_list.append(rain)
# print("連休の日にちと降水確率")
# print(rain_list)

# 旅行の日程期間の降水確率のデータ集め
rain_date = 0
rain_date_list = []
for lp3 in range(len(rain_list)):
    if lp3 == (len(rain_list) - (day[1] - 1)):
        break
    else:
        for lp4 in range(day[1]):
            rain_date += rain_list[lp3 + lp4][1]
        rain_date_list.append(rain_date)
        rain_date = 0
# print("各々の旅行期間の降水確率" + str(rain_date_list))

# 最小値を求める
trabel = rain_date_list.index(min(rain_date_list))
# print("最小のインデックスNO: " + str(trabel))

# 表示
print("{} {}".format(rain_list[trabel][0], rain_list[trabel + day[1] - 1][0]))