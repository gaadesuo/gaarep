import math

# データー入力
inp_list = []
road_list = []
ans_list = []
for lp0 in range(int(input())):
    inp_date = [int(lp1) for lp1 in input().split()]
    inp_list.append(inp_date)
    # 距離の計算 関数化できるか？
    long = (inp_date[0] ** 2) + (inp_date[1] ** 2)
    road = math.sqrt(long)
    road_list.append(road)

# print("入力座標" + str(inp_list))
# print("原点からの距離" + str(road_list))

# 判定 関数化予定
min_num = min(road_list)
if road_list.count(min_num) > 1:
    # road_listの要素の最小値のインデックスをリストに格納
    ind_list = [m_num for m_num, lp2 in enumerate(road_list) if lp2 == min_num]
    # print("最小値index" + str(ind_list))
    kari_point_list = []
    kari_road_list = []
    kari_ans = []
    kari_list = inp_list.copy()
    for lp3 in  ind_list:
        # print(str(lp3) + "番目")
        kari_list = inp_list.copy()
        del kari_list[lp3]
        kari_point = inp_list[lp3]
        # print(kari_list)
        # print(kari_point)
        for lp4 in kari_list:
            kyori_list = [abs(lp4[0] - kari_point[0]), abs(lp4[1] - kari_point[1])]
            kari_point_list.append(kyori_list)
            # print("次点座標から見た次の座標" + str(kari_point_list))
        for lp5 in kari_point_list:
            # 距離の計算 関数化できるか？
            kari_long = (lp5[0] ** 2) + (lp5[1] ** 2)
            kari_road = math.sqrt(kari_long)
            kari_road_list.append(kari_road)
            # print(kari_road_list)
        kari_min = min(kari_road_list)
        # 同一座標があるため最小値を削除
        del kari_road_list[kari_road_list.index(kari_min)]
        kari_ans.append(min(kari_road_list))
        kari_road_list = []
        kari_point_list = []
    kari_index = kari_ans.index(min(kari_ans))
    # 最小同一座標インデックスで最小座標をいれる
    kari_min_point = inp_list[ind_list[kari_index]]
    # print("同一距離座標の次点最短座標は" + str(kari_min_point))
    ans_list.append(kari_min_point)
    # 同一距離座標の次点最短座標を答えのリストに入れたので削除
    del inp_list[ind_list[kari_index]]
    # print("残った座標は" + str(inp_list))
    # 道のりのリストを初期化
    road_list = []
    for lp5 in inp_list:
        # 距離の計算 関数化できるか？
        long = (lp5[0] ** 2) + (lp5[1] ** 2)
        road = math.sqrt(long)
        road_list.append(road)
    # print(road_list)

    # ここからもう一度同じ距離がある場合18行目からの処理を繰り返す
    if road_list.count(min_num) > 1:
        print("関数へ")

    else:
        # 関数化する
        while len(inp_list) > 0:
            min_ind = road_list.index(min(road_list))
            ans_list.append(inp_list.pop(min_ind))

else:
    # 関数化する
    while len(inp_list) > 0:
        min_ind = road_list.index(min(road_list))
        ans_list.append(inp_list.pop(min_ind))

print(ans_list)

