# データー入力
time_list = []
for lp0 in range(int(input())):
    time = [lp1 for lp1 in input().split()]
    time_list.append(time)
# print(time_list)
time_date = [lp2 for lp2 in input().split()]
# print(time_date)
country = time_date[0]
con_time = time_date[1].split(":")
# print(country, con_time)

# 基準時間の検出
for lp3 in range(len(time_list)):
    if time_list[lp3][0] == country:
        base_time = int(con_time[0]) - int(time_list[lp3][1])
# print(base_time)

# 計算と表示
for lp4 in range(len(time_list)):
    add_time = int(time_list[lp4][1])
    ans_time = base_time + add_time
    while ans_time < 0 or ans_time > 23:
        if ans_time < 0:
            ans_time = 24 + ans_time
        elif ans_time > 23:
            ans_time = 24 - ans_time
    print("{:02d}:{:02d}".format(ans_time, int(con_time[1])))