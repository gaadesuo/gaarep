# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/08 :17:24$'


def inp_func():
    """
    基準となる数値nと距離の単位sが入力される
    1 <= n <= 1000
    m はkm, m, cm の3種類
    :return: 入力された文字列のリスト
    """
    inp_date = input().split()
    return inp_date[0], inp_date[1]


def math_func(n, m):
    """
    基準になる数字に単位ごとの倍率をかけてmmで返す
    n int 基準数値
    m str 単位
    :return: int 計算後の結果
    """
    ans_num = n * 10 if m == "cm" \
        else n * 100 * 10 if m == "m" \
        else n * 10 * 100 * 1000
    return ans_num


# ***処理***
num, unit = inp_func()
print("{:0d}".format(math_func(int(num), unit)))