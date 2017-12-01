import numpy as np


def word_check():
    """
    chech_wordがキーボードのどこにあるかを探し、x座標y座標を返す
    :return: list[x:int, y:int] x座標とy座標
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

    # print("")
    # print("今回判定する文字は【{}】".format(check_word))
    # 前回のキータッチでflagが立っているかの確認
    if grid_0[0] == 0 and grid_0[1] == 0:
        # print(grid_0)
        # 左手のリミットを触れた時
        if check_word in word_l:
            lr_hand = 1
            grid_0 = word_check()
            #   print("左手フラグ")
        # 右手のリミットを触れたとき
        elif check_word in word_r:
            lr_hand = 2
            grid_0 = word_check()
            # print("右手フラグ")

    # 前回flagが立ったままの場合
    else:
        grid_1 = word_check()
        # print("フラグが立ったので座標表示。前回の座標:{} 今回の座標{}".format(grid_0, grid_1))
        np_grid_0 = np.array(grid_0)
        np_grid_1 = np.array(grid_1)
        ans_grid = np_grid_0 - np_grid_1
        # print("引き算した座標は:{}".format(ans_grid))
        # キーが隣合わせかの確認 隣り合合わせなら無条件で座標入れ替え
        if (-1 <= ans_grid[0] <= 1 and ans_grid[1] == 0) or (
             -1 <= ans_grid[1] <= 1 and ans_grid[0] == 0):
            # print("隣り合わせになったのでキーのチェック")
            # 左手の時右側のキーならカウントアップ
            if lr_hand == 1:
                if check_word in all_word_r:
                    counter += 1
                    # print("左手で右をたたいたのでカウント:{:0d}".format(counter))
            # 右手の時左側のキーならカウントアップ
            else:
                if check_word in all_word_l:
                    counter += 1
                    # print("右手で左をたたいたのでカウント:{:0d}".format(counter))
            grid_0 = grid_1

        else:
            # print("隣り合わせ以外なのでリセット")
            grid_0 = [0, 0]
            lr_hand = 0
            # print("リセット後判定する文字は【{}】".format(check_word))
            # 前回のキータッチでflagが立っているかの確認
            if grid_0[0] == 0 and grid_0[1] == 0:
                # 左手のリミットを触れた時
                if check_word in word_l:
                    lr_hand = 1
                    grid_0 = word_check()
                    # print("左手フラグ")
                # 右手のリミットを触れたとき
                elif check_word in word_r:
                    lr_hand = 2
                    grid_0 = word_check()
                    # print("右手フラグ")

print(counter)

# lgabnyt
# リセットした後にフラグのチェックがされていない