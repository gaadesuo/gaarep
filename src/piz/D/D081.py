# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2017 / 11 / 23


"""
あなたは箱に入ったお菓子を家族 N 人で分けることにしました。
箱には縦に H 個、横に W 個の計 H × W 個のお菓子が入っていますが
N 人で均等にお菓子を分けた場合あまりが出る事があります。
N 人で均等にできるだけ多く分けた後のあまりのお菓子を出力してください。
・1 行目には家族の人数を表す整数 N が入力されます。

・2 行目には箱に入っているお菓子の、縦の数 H、横の数 W がこの順で半角スペース区切りで
入力されます。
・2 ≦ N ≦ 10
・1 ≦ H, W ≦ 50
・N, H, W は整数
"""

men = int(input())
box_okasi = [int(okasi) for okasi in input().split()]
ans = box_okasi[0] * box_okasi[1]
print("{:0d}".format(ans % men))
