# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "gaa"
__date__ = "$2017/03/08 7:12:43$"

import pygame
from pygame.locals import *
import sys




if __name__ == "__main__":


    pygame.init()

    msgothic = r'c:\windows\fonts\msgothic.ttc'

    #-----ウィンドウ作成-----


    #画面解像度
    SCREEN_SIZE = (640,480)
    screen = pygame.display.set_mode(SCREEN_SIZE)
    #ウィンドウタイトル
    pygame.display.set_caption(u"かゆうま日記")



    # フォントの作成
    myfont = pygame.font.Font(msgothic, 80)

    hello = myfont.render(u'かゆ　うま',True,(255,255,255))

    #-----ゲームループ-----
    while True:
        #背景の色
        screen.fill((0,0,0))

        screen.blit(hello, (20,60))

        pygame.display.update()

        for event in pygame.event.get():
            #終了イベントが発生したら終了する
            if event.type == QUIT:
                sys.exit()