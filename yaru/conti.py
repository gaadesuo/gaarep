# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "gaa"
__date__ = '$2017/03/19 :10:43$'

import pygame
from pygame.locals import *
import sys
import time

pygame.init()


"""-----

ファイルの読み込み

-----"""

# フォントファイルの読み込み
mona = r'c:\windows\fonts\ipagp-mona.ttf'

# 画像ファイルの読み込み

bg = r"C:\Users\user\Documents\NetBeansProjects\gaarep\PythonProject\yaruo\BG.png"

"""-----

フォントの設定

-----"""

font_20 = pygame.font.Font(mona, 20)

"""-----

文字レンダリング

-----"""

TITLE_NAME_U = font_20.render("やる夫が", True, (255, 255, 255))

"""-----

ウィンドウ作成

-----"""

# 画面解像度
SCREEN_SIZE = (1024, 768)
screen = pygame.display.set_mode(SCREEN_SIZE)

"""-----

画像処理

-----"""

# 背景
BG = pygame.image.load(bg).convert()


def con():
    screen.blit(BG, (0, 0))
    pygame.display.update()

    screen.blit(TITLE_NAME_U, (40, 20))
    time.sleep(1)