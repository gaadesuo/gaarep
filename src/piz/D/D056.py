# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/18 :15:36$'


def inp_func():
    """
    成する立方体の 1 辺の長さ (m) を表す整数
    r_1, r_2 が半角スペース区切りで与えられるのでそれを返す
    1 ≦ r_2 < r_1 ≦ 20
    :return: int 入力された一片の長さ2つ
    """
    r_list = [int(s) for s in input().split()]
    return r_list[0], r_list[1]


def necessary_snow_func(r_1, r_2):
    """
    1 辺が r1 (m) の立方体から r2 (m) の立方体分をくり抜く形のかまくらを作るときの
    必要な体積を求める
    :param r_1:int かまくらの一辺の長さ
    :param r_2:int くりぬく立方体の一辺の長さ
    :return: かまくらを作るのに必要な体積
    """
    ans_num = (r_1 ** 3) - (r_2 ** 3)
    return ans_num


# ***処理***
out_r, in_r = inp_func()
print("{:0d}".format(necessary_snow_func(out_r, in_r)))