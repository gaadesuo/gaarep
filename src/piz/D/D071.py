# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/11/21 :17:39$'


def inp_func():
    """
    気温を表す整数 t と、湿度を表す整数 m がスペース区切りで入力されるのでそれを返す
    :return: int 気温と湿度
    """
    num_list = [int(num) for num in input().split()]
    return num_list[0], num_list[1]


def laundry_func(t, m):
    """
    気温が 25 ℃以上の日、もしくは湿度が 40 % 以下の日は干し。それ以外の日は干さない。
    ただし、上記の干す条件を満たす日のうち、気温が 25 ℃以上かつ、湿度 40 % 以下の
    日は砂ぼこりが舞うので干しません。
    :param t: 気温
    :param m: 湿度
    :return: str 干す場合は "Yes" 干さない場合は "No" を返す
    """
    if t >= 25 or m <= 40:
        if t >= 25 and m <= 40:
            return "No"
        return "Yes"
    else:
        return "No"


# ***処理***
temp, humi = inp_func()
print("{}".format(laundry_func(temp, humi)))