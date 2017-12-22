# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2017 / 11 / 21

import numpy as np

def grid_check(w):
    """
    与えられた文字の座標を調べて返す
    :param w: 調べる文字列
    :return: list[X座標, Y座標]
    """
    temp_grid = [0,0]
    if w in all_key_list[0]:
        temp_grid[1] = 1
        temp_grid[0] = (list(all_key_list[0]).index(w) + 1)
    elif w in all_key_list[1]:
        temp_grid[1] = 2
        temp_grid[0] = (list(all_key_list[1]).index(w) + 1)
    else:
        temp_grid[1] = 3
        temp_grid[0] = (list(all_key_list[2]).index(w) + 1)
    return  temp_grid


def limit_check(w):
    """
    左右キー間違いのリミット文字を触れたか確認。
    左のリミットならフラグ1右手ならフラグ2を代入し1を返す
    :param w: チェックする文字
    :return: リミットに触れない:0, リミットに触れた:1
    """
    global hand_check
    global old_grid

    if w in left_key_list[0]:
        hand_check = 1
    elif w in right_key_list[0]:
        hand_check = 2
    if hand_check > 0:
        old_grid = grid_check(w)
        print("リミットの文字を触れた。文字列【{}】のX座標は: {}, Y座標は: {}".format(
            word, old_grid[0], old_grid[1]))
        return 1
    return 0


all_key_list = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
left_key_list = ["tgb","qwertasdfgzxcvb"]
right_key_list = ["yhn","yuiophjklnm"]
old_grid = [0, 0]
new_grid = [0, 0]
hand_check = 0
flag = 0
counter = 0

inp_word = list(input())
# print("入力された文字列は: {}".format(inp_word))


for word in inp_word:
    print("文字列【{}】チェック".format(word))
    # 前回リミットフラグを立ててないかの確認
    if flag == 0:
        flag = limit_check(word)

    # リミットフラグが成立
    elif flag == 1:
        new_grid = grid_check(word)

        # 新旧の座標差を比べて隣接しているか確認
        np_old = np.array(old_grid)
        np_new = np.array(new_grid)
        diff_grid = np_new - np_old
        print("座標差の確認 旧: {} 新: {} 差: {}".format(old_grid, new_grid, diff_grid))
        if ((diff_grid[0] == -1 or diff_grid[0] == 0 or diff_grid[0] == 1) and diff_grid[1] == 0) or (
                (diff_grid[1] == -1 or diff_grid[1] == 0 or diff_grid[1] == 1) and diff_grid[0] == 0):
            print("文字【{}】は前回と隣接している".format(word))
            # リミットを触れたときが左手で今回右側のキーをタッチしている
            if hand_check == 1 and word in right_key_list[1]:
                counter += 1
            # リミットを触れたときが右手で今回左側のキーをタッチしている
            elif hand_check == 2 and word in left_key_list[1]:
                counter +=1
            old_grid = new_grid
        else:
            print("隣接しなくなったので初期化")
            hand_check = 0
            old_grid = [0, 0]
            flag = 0
            flag = limit_check(word)

print(counter)

