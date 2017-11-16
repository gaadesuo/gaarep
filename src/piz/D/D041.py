# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/16 :10:19$'


def inp_func():
    """
    本の幅を合計したもの n (cm)、検討している本棚の段数 d
    本が収まる幅 e (cm)がそれぞれ半角スペース区切りで与えられる
    半角スペースで分けてリストへ入れる
    ・入力される値はすべて整数
    ・1 ≦ n ≦ 500
    ・1 ≦ d ≦ 10
    ・1 ≦ e ≦ 500
    :return: 入力された数字のリスト
    """
    inp_list = [int(num) for num in input().split()]
    return inp_list[0], inp_list[1], inp_list[2]


def bookshelf_func(n, d, e):
    """
    購入予定の本棚の収まる幅e、段数dを掛けたものと本の幅の合計nを比較し
    本棚に本が入るかを判定すして結果を返す
    :return: str 入るなら'OK' 入らないなら'NG'
    :param n: int 本の幅の合計
    :param d: int 本棚の段数
    :param e: int 本棚の入る幅
    :return: str 入るなら'OK' 入らないなら'NG'
    """
    ans_word = "NG" if n > (d * e) else "OK"
    return ans_word


# ***処理***
books_width, shelf_width, shelf_stage = inp_func()
print("{}".format(bookshelf_func(books_width, shelf_width, shelf_stage)))
