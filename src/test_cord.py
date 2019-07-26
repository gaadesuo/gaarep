#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2019/07/18 18:11'

import sys
import math


def end():
    """
    終了する
    """
    sys.exit()


def p_to_t():
    """
    モーターの出力からトルクを求める
    """
    w = input("モーター出力の定格回転数がわからない場合は【y】を入力")
    if w == "y":
        magnet_pole = int(input("モーターの極数を入力 【半角英数のみ】"))
        s = int(input("すべりを入れてください。単位: % 【半角数字】"))
        print("""定格回転数Nを求める公式は 
        N = 120 * 50(関東周波数) / p(極数) * (1 - (s / 100)) (すべり割合)の為 
        """)
        print("N = 120 * 50 / {} * (1 - ({} ? 100))".format(magnet_pole, s))
        ans = 120 * 50 / magnet_pole * (1 - (s / 100))
        print("定格回転数【{}】rpm".format(ans))

    w = 0
    w = input("モーターのトルクを求める場合は【y】を入力")
    if w == "y":
        pw = float(input("モーターの出力を入力 単位: kw 【半角数字】"))
        n = int(input("定格回転数を入力 単位: min 【半角数字】"))

        print("""モーターの出力を求める公式は
        P:モーター出力
        N:定格回転数
        T:トルク
        とすると。
        P = (2 * π * N * T) / (102 * 60)
        になる。
        
        両辺に(102 * 60)を掛けて右辺のそれを打ち消す
        P * (102 * 60) = 2 * π * N * T
        そして両辺を(2 * π * N)で割ってやるとTの値が求まる
        p * (102 * 60) / (2 * π * N) = T        
        """)
        t = pw * (102 * 60) / (2 * math.pi * n)
        print("トルクは: {}kg･m".format(t))
        return t


def t_to_p():
    """
    必要トルクからモーターの出力を求める
    """
    print("今回は400kgの重量なので上げる力の値は400kgf")
    l = float(input("モーター巻取り部の半径の長さ 単位:m 【半角英数】"))
    print("ギア比は不明なのでわかったら追加")

    print("必要なトルクの値は: 400kgf * {}(巻取り径の半径) なので")
    ans_torque = 400 * l
    print("{}kgf･m".format(ans_torque))

    print("必要な出力を求める")
    print("""モーターの出力を求める公式は
    P(kw) = (2 * π * N(回転数) * T(トルク)) / (102 * 60)
    なので回転数を入れてやれば適正な出力か判断できる""")
    n = int(input("回転数を入力 単位: rpm 【半角数字】"))
    print("トルクは先ほどの答えを代入")
    print("p(kw) = (2 * π * {} * {}) / (102 * 60)".format(n, ans_torque))
    p = (2 * math.pi * n * ans_torque) / (102 * 60)
    print("{} kw".format(p))


def torque():
    """
    トルクの計算式
    :return:02
    f = 0
    n = 0
    """
    w = input("kgfの場合は【k】Nの場合は【n】終了は【e】を入力")
    if w == "k":
        f = float(input("kgfの値を入力 単位:kgf【半角数字のみ】"))
        n = 9.8 * f

    elif w == "n":
        n = float(input("Nの値を入力 単位:N 【半角数字のみ】"))
        # 1N = 1/9.8 ∴0.102kgf
        f = (0.102 * n)

    elif w == "e":
        end()

    l = float(input("長さの値を入力 単位:m 【半角数字のみ】"))

    print("トルクの値")
    print("{}kgf･m".format(f * l))
    print("{}N･m".format(n * l))


def main():
    t_to_p()


if __name__ == '__main__':
    main()
