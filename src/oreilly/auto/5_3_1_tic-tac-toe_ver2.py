# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/06 04:47'

import copy as cp

num_list = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

turn = 1
win = 0


def p_board(list_0):
    """
    現在の碁盤を表示する
    :param list: 入力されたキーに対応する数字のリスト
    """
    l = cp.deepcopy(list_0)
    for ind_0 in range(len(l)):
        for ind_1 in range(len(l[ind_0])):
            # print(l[ind_0][ind_1])
            if l[ind_0][ind_1] == 0:
                l[ind_0][ind_1] = " "
            elif l[ind_0][ind_1] == 1:
                l[ind_0][ind_1] = "o"
            elif l[ind_0][ind_1] == -1:
                l[ind_0][ind_1] = "x"
    # print(l)
    print("{}|{}|{}".format(l[0][0], l[0][1], l[0][2]))
    print("-+-+-")
    print("{}|{}|{}".format(l[1][0], l[1][1], l[1][2]))
    print("-+-+-")
    print("{}|{}|{}".format(l[2][0], l[2][1], l[2][2]))
    print("")
    print("*** 入力対応キー ***")
    for i in range(1, 10):
        print(i, end="")
        if i == 3 or i == 6:
            print(" ")
    print("")


def inp_num():
    """
    入力対応キーで対応する座標に数字を入れる
    """
    global num_list
    global turn
    while True:
        try:
            n = int(input(">>> "))
            if n < 1 or 9 < n:
                print("1～9までの半角英数を入れてください")
                continue
            # print(int((n - 1) / 3), (n - (3 * int((n - 1) / 3))) - 1)
            if num_list[int((n - 1) / 3)][n - (3 * int((n - 1) / 3)) - 1] != 0:
                print("すでに打たれている場所なので別の場所を選んでください。")
                continue
            num_list[int((n - 1) / 3)][n - (3 * int((n - 1) / 3)) - 1] = turn
            # print(num_list)
            turn = -1 if turn == 1 else 1
            # print(turn)
            break

        except ValueError:
            print("半角数字で入れてください")


def decision(list_1):
    """
    勝敗判定 各ラインの合計値が３ならフラグに1、-3ならフラグに-1を代入
    リストから0がなくなったら引き分け
    :param list_1: 入力されたキーに対応する数字のリスト
    """
    global win
    a = 0
    b = 0

    # 縦横ライン判定
    for i_0 in range(3):
        for i_1 in range(3):
            a += list_1[i_0][i_1]
            b += list_1[i_1][i_0]
            if a == 3 or b == 3:
                win = 1
            elif a == -3 or b == -3:
                win = -1
        a = 0
        b = 0

    # 斜め判定
    c = list_1[0][0] + list_1[1][1] + list_1[2][2]
    d = list_1[0][2] + list_1[1][1] + list_1[2][0]
    if c == 3 or d == 3:
        win = 1
    elif c == -3 or d == -3:
        win = -1

    # 引き分け判定
    if 0 not in list_1[0] and 0 not in list_1[1] and 0 not in list_1[2]:
        win = 3


def main():
    while True:
        p_board(num_list)
        if turn == 1:
            print("")
            print("先手です。入力対応キーを押してください")
        else:
            print("")
            print("後手です。入力対応キーを押してください")
        inp_num()
        # print(num_list)
        decision(num_list)
        if win == 1:
            p_board(num_list)
            print("*** おめでとう、先手の勝ちです。***")
            break
        elif win == -1:
            p_board(num_list)
            print("*** おめでとう、後手の勝ちです。***")
            break
        elif win == 3:
            p_board(num_list)
            print("*** 今回は引き分けでした ***")
            break


if __name__ == '__main__':
    main()
