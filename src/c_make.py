#! /usr/bin/python
# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "gaa"
__date__ = "$2017/03/07 23:23:02$"

import random


def dice():
    return (random.randint(1,601) % 6) + 1
'''
サイコロの数値1～6の数値を返す
'''


print('''
＊＊＊ キャラクターを作成します ＊＊＊
''')

while True:

    name = input(u'名前を入れてください　>>>')
    print(u'''
    あなたの名前は{}です。
    続いて、パラメーターを作成します。ダイスを3回振ってください。
    '''.format(name))

    comand = input(u'ダイスを振ります。エンターを押してください >>>')
    D_ATK = dice()
    print(D_ATK)

    comand = input(u'ダイスを振ります。エンターを押してください >>>')
    D_DEF = dice()
    print(D_DEF)

    comand = input(u'ダイスを振ります。エンターを押してください >>>')
    D_HP = dice()
    print(D_HP)
    MHP = D_HP + 18

    print('''パラメーターが決定しました
    あなたの名前     {}
    あなたの攻撃力   {}
    あなたの防御力   {}
    あなたの最大体力 {}
    '''.format(name,D_ATK,D_DEF,MHP))

    inp = input('''上記のキャラクターでよろしいですか？
作成を完了する場合はyを入力してください。
やり直す場合はそれ以外のキーを入力してください
>>> ''')

    if inp == 'y':
        break
    else:
        continue

print(u'＊＊＊ キャラクターが完成しました ＊＊＊')