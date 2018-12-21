#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = "2018/12/19 22:50"

# 入力
word =""
try:
    with open("B047", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            word = txt.strip()
        inp_txt.close()

except FileNotFoundError:
    word = input()

print("入力文字: {}".format(word))

# 処理


def index_search(l, w):
    """
    与えられた左、右手のフラグリストに与えられた文字がある場合そのインデックスを返す
    :param l: 左、右のフラグリスト
    :param w: 検索文字
    :return: HITした文字のインデックス
    """
    return l.index(w) if w in l else 255


def key_index(l, w):
    """
    keyリストの中から与えられた文字のインデックスを返す
    :param l: keyリスト
    :param w: 検索文字
    :return: x, y座標
    """
    x = 0
    y = 0
    for y, s in enumerate(l):
        try:
            x = s.index(w)
            break
        except ValueError:
            pass
    return x, y


key_type = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
            ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
            ["z", "x", "c", "v", "b", "n", "m"]]
l_flag = ["t", "g", "b"]
r_flag = ["y", "h", "n"]
word_list = list(word)
flag = 0
counter = 0
x_grid = 0
y_grid = 0
x_after = 0
y_after = 0

# thgy で通らない
for s in word_list:
    # 左手のフラグは1、右手は2、それ以外は0
    if flag == 0:
        # print("文字: {}, 左手フラグ{}, 右手フラグ{}".format(s, index_search(l_flag, s), index_search(r_flag, s)))
        if index_search(l_flag, s) == 255 and index_search(r_flag, s) == 255:
            pass
        elif index_search(l_flag, s) != 255:
            flag = 1
            x_grid, y_grid = key_index(key_type, s)
            # print("立ったフラグNO: {}, x座標: {}, y座標: {}".format(flag, x_grid, y_grid))
        elif index_search(r_flag, s) != 255:
            flag = 2
            x_grid, y_grid = key_index(key_type, s)
            # print("立ったフラグNO: {}, x座標: {}, y座標: {}".format(flag, x_grid, y_grid))
    elif flag > 0:
        x_after, y_after = key_index(key_type, s)
        print("フラグ立ってる時 x座標: {}, y座標: {}".format(x_after, y_after))
        if ((x_grid == x_after) and (y_grid - 1 <= y_after <= y_grid + 1)) \
                or ((y_grid == y_after) and (x_grid - 1 <= x_after <= x_grid + 1)):
            if ((flag == 1) and (x_after > 4)) or ((flag == 2) and (x_after < 5)):
                # print("x座標一マスずれ")
                x_grid = x_after
                y_grid = y_after
                counter += 1
            else:
                x_grid = x_after
                y_grid = y_after
        else:
            x_grid = 0
            y_grid = 0
            flag = 0
print(counter)