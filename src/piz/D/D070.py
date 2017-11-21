# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/21 :17:38$'


def inp_func():
    """
    本の総ページ数 m と読み終えたページ数 n がスペース区切りで与えられるのでそれを返す
    ・m, n は整数
    ・1 ≦ n < m ≦ 100
    :return: int 総ページと読んだページ
    """
    num_list = [int(num) for num in input().split()]
    return num_list[0], num_list[1]


def remain_page_func(m, n):
    """
    本の総ページ数とみ終えたページから残りのページ数を表示する
    :param m:int 本の総ページ
    :param n:int 本を読み終えたページ
    :return: int 残りのページ
    """
    ans_num = m - n
    return ans_num


# ***処理***
all_page, reading_page= inp_func()
print("{:0d}".format(remain_page_func(all_page, reading_page)))