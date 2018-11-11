#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/10 10:59'


def print_table(list):
    """
    各リストの要素を後ろ合わせで縦に表記する
    :param list: 表示する文字列のリスト
    """
    num_list = []
    new_list = []
    print_list = []

    # 表示時の段数分のリストを作る
    for i in range(len(list[0])):
        print_list.append([])
    # print(print_list)

    # リストの中の最大文字数に合わせ右揃えにする
    for l in list:
        for w in l:
            num_list.append(len(w))
        # print(num_list)
        m_num = max(num_list)
        for i in range(len(l)):
            l[i] = l[i].rjust(m_num)
        # print(l)
        new_list.append(l)
        num_list = []
    # print(new_list)

    # リストの要素を表記順に並べなおす
    for i_0 in range(len(new_list)):
        for i_1 in range(len(new_list[i_0])):
            # print(new_list[i_0][i_1])
            print_list[i_1].append(new_list[i_0][i_1])
            # print(print_list)

    # 表示
    for l in print_list:
        print(" ".join(l))


def main():
    table_date = [["apples", "oranges", "cherries", "banana"],
                  ["Alice", "Bob", "Carol", "David"],
                  ["dogs", "cats", "moose", "goose"]]

    print_table(table_date)


if __name__ == '__main__':
    main()