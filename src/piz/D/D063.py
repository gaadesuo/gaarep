# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/20 :08:11$'


def inp_func():
    """
    1 行目に 5 つの整数tが半角スペース区切りで与えられます
    2 行目にあなたがお花見会場に到着する時刻 (分) を表す整数 a が与えられます
    t行の数値をリストにして、aは数値で返す
    ・0 ≦ t1 < t2 < t3 < t4 < t_5 ≦ 59
    ・0 ≦ a ≦ 59
    ・a は t1, t2, t3, t4, t_5 のいずれとも一致しない
    :return: list[int(t)] int(a)
    """
    t_list = [int(t) for t in input().split()]
    a = int(input())
    return t_list, a


def ascending_order_conf(t_list, a):
    """
    あなた以外の 5 人の到着する時刻 (分) t_list
    とあなたの計画する到着予定時刻 (分) aが与えられるので
    このとき 6 人の中であなたが何番目に到着するかを求めて返す
    :param t_list: list[int] 5人の到着する時間のリスト
    :param a: int 自分の到着予定時間
    :return: int 何番目か
    """
    ans_num = 1
    for minits in t_list:
        if minits > a:
            return ans_num
        else:
            ans_num += 1
    return ans_num


# ***処理***
other_min, mine_min = inp_func()
print("{:0d}".format(ascending_order_conf(other_min, mine_min)))