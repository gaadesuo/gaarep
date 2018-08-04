# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/08/04 09:42'


def grid_change(grid_list):
    """
    リストの要素を読み込み座標を変え縦表示にする
    :param grid_list: グリッドのリスト
    """
    x_num = 6
    y_num = 9

    for i in range(x_num):
        for j in range(y_num):
            print("\n" if j == 8 else grid_list[j][i], end="")


def main():
    grid = [[".", ".", ".", ".", ".", "."],
            [".", "o", "o", ".", ".", "."],
            ["o", "o", "o", "o", ".", "."],
            ["o", "o", "o", "o", "o", "."],
            [".", "o", "o", "o", "o", "o"],
            ["o", "o", "o", "o", "o", "."],
            ["o", "o", "o", "o", ".", "."],
            [".", "o", "o", ".", ".", "."],
            [".", ".", ".", ".", ".", "."]]

    grid_change(grid)


if __name__ == '__main__':
    main()