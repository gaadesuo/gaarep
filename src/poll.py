#! /usr/bin/python
# -*- cording: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "user"
__date__ = "$2017/02/20 20:41:19$"


#-----初期設定-----

vipper = {}
neler = []


#-----入力開始-----


#集計するときはend:を入れる
while True:
    print(u'AAキャラで誰が好きですか？')
    name = input(u' >>> ')
    if name == 'end:':
        break


    #-----入力確認-----


    print(u'入力された名前は【' + str(name) + u'】です。よろしければ\'y\'を、直したい場合は\'n\'を押してください')
    while True:
        yn = input(' >>> ')
        if (yn == u'y') or (yn == u'n') or (yn == u'ｙ') or (u'ｎ'):
            break
        print(u'よろしければ\'y\'を、直したい場合は\'n\'を入れてください')
        continue
    if (yn == u'n') or (yn == u'ｎ'):
        continue
    neler.append(name)


#-----集計-----


#以下の行はsyntax errorでダメ。どうやら辞書の内包の条件演算でelse付きはだめらしい？
#ifのみなら下記の奴で行けるが下記もうまくいってない
# vipper = {men:+1 if men in neler else men:1 for men in neler}

#下記の2行だと+1が計算されない
#vipper = {men:+1 for men in neler if men in vipper}
#vipper = {men:1 for men in neler}

for men in neler:
    if men in vipper:
        vipper[men] += 1
    else:
        vipper[men] = 1


#-----結果表示-----


#下記2行だと表記時に得票数でソートされない
#for name,slip in vipper.items():
#    print(name,slip)
#なのでsorted関数を使って且つラムダ式を使う。これは関数の勉強で出てくるっぽい。
for name,slip in sorted(vipper.items(), key=lambda x:x[1]):
    print(name,slip)
