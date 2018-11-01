# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/08/04 18:35'


def display_inventry(inventory):
    """
    インベントリの中身とアイテムの総数を表示
    :param inventory: インベントリの中身の辞書
    """
    count_num = 0
    print("持ち物リスト:")
    for k, v in inventory.items():
        count_num += v
        print("{} {}".format(v, k))
    print("アイテム総数: {}".format(count_num))


def main():
    item_dic = {"矢": 12, "金貨": 42, "ロープ": 1, "たいまつ": 6, "手裏剣": 1}
    display_inventry(item_dic)


if __name__ == '__main__':
    main()