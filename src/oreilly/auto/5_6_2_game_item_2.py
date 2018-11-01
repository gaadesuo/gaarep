# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/08/04 19:13'


def add_to_inventory(inventory, added_items):
    """
    持ち物リストにドロップしたアイテムを追加する
    :param inventory: インベントリの辞書
    :param added_items: ドロップアイテム
    :return: 追加してインベントリの辞書
    """
    for name in added_items:
        inventory.setdefault(name, 0)
        inventory[name] += 1
    return inventory


def display_inventory(inventory):
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
    inv = {"金貨": 42, "ロープ": 1}
    dragon_loot = ["金貨", "手裏剣", "金貨", "金貨", "ルビー"]
    inv = add_to_inventory(inv, dragon_loot)
    display_inventory(inv)


if __name__ == '__main__':
    main()