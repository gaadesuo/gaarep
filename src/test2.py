import numpy as np


def word_check():
    """
    """
    if check_word in all_word[0]:
        l_grid_no = [all_word[0].find(check_word), 0]
        return l_grid_no
    elif check_word in all_word[1]:
        l_grid_no = [all_word[1].find(check_word), 1]
        return l_grid_no
    else:
        l_grid_no = [all_word[2].find(check_word), 2]
        return l_grid_no


all_word = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
all_word_l = "qwertasdfgzxcvb"
all_word_r = "yuiophjklnm"
word_l = "tgb"
word_r = "yhn"

grid_0 = [0, 0]
grid_1 = [0, 0]
lr_hand = 0
counter = 0

inp_word = list(input())
for check_word in inp_word:
    # 前回のキータッチでflagが立っているかの確認
    if grid_0[0] == 0 and grid_0[1] == 0:
        # 左手のリミットを触れた時
        if check_word in word_l:
            lr_hand = 1
            grid_0 = word_check()
        # 右手のリミットを触れたとき
        elif check_word in word_r:
            lr_hand = 2
            grid_0 = word_check()

    # 前回flagが立ったままの場合
    else:
        grid_1 = word_check()
        # print("フラグが立ったので座標表示。前回の座標:{} 今回の座標{}".format(grid_0, grid_1))
        np_grid_0 = np.array(grid_0)
        np_grid_1 = np.array(grid_1)
        ans_grid = np_grid_0 - np_grid_1
        # キーが隣合わせかの確認 隣り合合わせなら無条件で座標入れ替え
        if (ans_grid[0] == -1 or ans_grid[0] == 0 or ans_grid[0] == 1) and (
                    ans_grid[1] == -1 or ans_grid[1] == 0 or ans_grid[1] == 1):
            # 左手の時右側のキーならカウントアップ
            if lr_hand == 1:
                if check_word in all_word_r:
                    counter += 1
            # 右手の時左側のキーならカウントアップ
            else:
                if check_word in all_word_l:
                    counter += 1
            grid_0 = grid_1

        else:
            grid_0 = [0, 0]
            lr_hand = 0

print(counter)