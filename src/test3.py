import numpy as np

all_word = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
side_limit = list("yhntgb")

inp_word = list(input())

counter = 0
grid_0 = [0, 0]
grid_1 = [0, 0]
for check_word in inp_word:
    # 前回間違えぎりぎりのフラグが立ってない場合
    if grid_0[0] == 0 and grid_0[1] == 0:
        if check_word in side_limit:
            # 間違えぎりぎりをタッチしたので文字からx, y座標を求める
            if check_word in all_word[0]:
                grid_0 = [all_word[0].find(check_word), 0]
            elif check_word in all_word[1]:
                grid_0 = [all_word[0].find(check_word), 1]
            else:
                grid_0 = [all_word[0].find(check_word), 2]

    # 前回間違えのフラグが立ってる場合
    else:
        print("flagが立ってるため前回の座標チェック x:{:0d}, y:{:0d}".format(grid_0[0], grid_0[1]))
        # 今回の座標取得
        if check_word in all_word[0]:
            grid_1 = [all_word[0].find(check_word), 0]
        elif check_word in all_word[1]:
            grid_1 = [all_word[0].find(check_word), 1]
        else:
            grid_1 = [all_word[0].find(check_word), 2]

        # 座標が前回と近似値かどうかの確認。近似値ならカウントしgrid_0上書き。違う場合はgrid_0初期化
        np_grid_0 = np.array(grid_0)
        np_grid_1 = np.array(grid_1)
        diff_grid = np_grid_0 - np_grid_1
        print("前回との座標の差異 x:{:0d}, y:{:0d}".format(diff_grid[0], diff_grid[1]))
        if (-1 <= diff_grid[0] <= 1 and diff_grid[1] == 0)\
                or (-1 <= diff_grid[1] <= 1 and diff_grid[0] == 0):
            counter += 1
            grid_0 = grid_1
        else:
            grid_0 = [0, 0]

print(counter)

# 右手と左手判別
右手が左に行った後みぎてにもどったらかうんとしない