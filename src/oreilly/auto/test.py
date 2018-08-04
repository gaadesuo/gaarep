# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/08/04 17:26'


def total_brought(guests, item):
    num_brought = 0
    for v in guests.values():
        num_brought = num_brought + v.get(item, 0)
    return num_brought


def main():
    all_guests = {"アリス": {"リンゴ": 5, "ブレッツェル": 112},
                  "ボブ": {"ハムサンド": 3, "リンゴ": 2},
                  "キャロル": {"コップ": 3, "アップルパイ": 1}}
    print("持ち物の数")
    print(" - リンゴ " + str(total_brought(all_guests, "リンゴ")))
    print(" - コップ " + str(total_brought(all_guests, "コップ")))
    print(" - ケーキ " + str(total_brought(all_guests, "ケーキ")))
    print(" - ハムサンド " + str(total_brought(all_guests, "ハムサンド")))
    print(" - アップルパイ " + str(total_brought(all_guests, "アップルパイ")))


if __name__ == '__main__':
    main()