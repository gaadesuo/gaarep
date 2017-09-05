import math


def road_fnc(x_grid, y_grid):
    """
    座標から直線距離を求めて返す
    :param x_grid: X座標
    :param y_grid: Y座標
    :return: 直線距離(float)
    """
    long = (x_grid ** 2) + (y_grid ** 2)
    return math.sqrt(long)


def grid_list_sort_fnc(grid_list, road_list):
    """
    直線距離のリストの中の最小値を求め小さい順からリストに入れる
    :param grid_list: 座標list
    :param road_list: 距離list
    :return: 座標(list)
    """
    fnc_ans = []
    while len(grid_list) > 0:
        # print("座標" + str(grid_list))
        min_ind = road_list.index(min(road_list))
        fnc_ans.append(grid_list.pop(min_ind))
        del road_list[min_ind]
    return fnc_ans


# データー入力
inp_list = []
road_list = []
ans_list = []
for lp0 in range(int(input())):
    inp_date = [int(lp1) for lp1 in input().split()]
    inp_list.append(inp_date)
    road_list.append(road_fnc(inp_date[0], inp_date[1]))   # 距離計算の関数呼び出し


# print("入力座標" + str(inp_list))
# print("原点からの距離" + str(road_list))

# 判定 関数化予定
min_num = min(road_list)
if road_list.count(min_num) > 1:
    ind_list = [m_num for m_num, lp2 in enumerate(road_list) if lp2 == min_num]   # road_listの要素の最小値のインデックスをリストに格納
    # print("最小値index" + str(ind_list))
    tmp_grid_list = []
    tmp_road_list = []
    tmp_ans = []
    tmp_list = inp_list.copy()
    for lp3 in ind_list:
        # print(str(lp3) + "番目")
        tmp_list = inp_list.copy()
        del tmp_list[lp3]
        kari_point = inp_list[lp3]
        # print(kari_list)
        # print(kari_point)
        for lp4 in tmp_list:
            kyori_list = [abs(lp4[0] - kari_point[0]), abs(lp4[1] - kari_point[1])]
            tmp_grid_list.append(kyori_list)
            # print("次点座標から見た次の座標" + str(kari_point_list))
        for lp5 in tmp_grid_list:
            tmp_road_list.append(road_fnc(lp5[0], lp5[1]))   # 距離計算の関数呼び出し
            # print(kari_road_list)
        kari_min = min(tmp_road_list)
        del tmp_road_list[tmp_road_list.index(kari_min)]   # 同一座標があるため最小値を削除
        tmp_ans.append(min(tmp_road_list))
        tmp_road_list = []
        tmp_grid_list = []
    kari_index = tmp_ans.index(min(tmp_ans))
    kari_min_point = inp_list[ind_list[kari_index]]   # 最小同一座標インデックスで最小座標をいれる
    # print("同一距離座標の次点最短座標は" + str(kari_min_point))
    ans_list.append(kari_min_point)
    del inp_list[ind_list[kari_index]]   # 同一距離座標の次点最短座標を答えのリストに入れたので削除
    # print("残った座標は" + str(inp_list))
    road_list = []
    for lp5 in inp_list:
        road_list.append(road_fnc(lp5[0], lp5[1]))
    # print(road_list)

    # ここからもう一度同じ距離がある場合18行目からの処理を繰り返す
    # でバック中.本来は   if road_list.count(min_num) > 1:
    if road_list.count(min_num) == 99999:
        print("関数へ")

    else:
        for grid_num in (grid_list_sort_fnc(inp_list, road_list)):   # 関数内で小さい順に返されたリストを答えのリストに入れる
            ans_list.append(grid_num)

else:
    for grid_num in (grid_list_sort_fnc(inp_list, road_list)):   # 関数内で小さい順に返されたリストを答えのリストに入れる
        ans_list.append(grid_num)

# 表示
for ans_grid in ans_list:
    print("{} {}".format(ans_grid[0], ans_grid[1]))
