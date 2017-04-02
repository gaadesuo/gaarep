# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/00/00 :00:00$'

import pygame
from pygame.locals import *
import sys
import time
import conti
import random

pygame.init()

"""-----

ファイルの読み込み

-----"""

# フォントファイルの読み込み
mona = r'c:\windows\fonts\ipagp-mona.ttf'

# 画像ファイルの読み込み

bg = r"C:\Users\user\Documents\NetBeansProjects\gaarep\PythonProject\yaru\image\BG.png"
menu_1 = r"C:\Users\user\Documents\NetBeansProjects\gaarep\PythonProject\yaru\image\m1.gif"
menu_2 = r"C:\Users\user\Documents\NetBeansProjects\gaarep\PythonProject\yaru\image\m2.gif"
menu_3 = r"C:\Users\user\Documents\NetBeansProjects\gaarep\PythonProject\yaru\image\m3.gif"
menu_4 = r"C:\Users\user\Documents\NetBeansProjects\gaarep\PythonProject\yaru\image\m4.gif"
menu_5 = r"C:\Users\user\Documents\NetBeansProjects\gaarep\PythonProject\yaru\image\m5.gif"
menu_6 = r"C:\Users\user\Documents\NetBeansProjects\gaarep\PythonProject\yaru\image\m6.gif"
menu_7 = r"C:\Users\user\Documents\NetBeansProjects\gaarep\PythonProject\yaru\image\m7.gif"
menu_8 = r"C:\Users\user\Documents\NetBeansProjects\gaarep\PythonProject\yaru\image\m8.gif"
menu_9 = r"C:\Users\user\Documents\NetBeansProjects\gaarep\PythonProject\yaru\image\m9.gif"
menu_0 = r"C:\Users\user\Documents\NetBeansProjects\gaarep\PythonProject\yaru\image\m0.gif"
yaruo = r"C:\Users\user\Documents\NetBeansProjects\gaarep\PythonProject\yaru\image\titleyaru.png"
down = r"C:\Users\user\Documents\NetBeansProjects\gaarep\PythonProject\yaru\image\downBG.png"
stat = r"C:\Users\user\Documents\NetBeansProjects\gaarep\PythonProject\yaru\image\statwind.png"


"""-----

フォントの設定

-----"""

font_100 = pygame.font.Font(mona, 100)
font_50 = pygame.font.Font(mona, 50)
font_40 = pygame.font.Font(mona, 40)
font_20 = pygame.font.Font(mona, 20)

"""------

関数の作成

-----"""


def operation():
    """
    マウス、キーボード等のpolling処理
    returns: int
    """

    for event in pygame.event.get():
        # 終了イベントが発生したら終了する
        if event.type == QUIT:
            sys.exit()
    pressed_mouse = pygame.mouse.get_pressed()
    if pressed_mouse[0]:
        x, y = pygame.mouse.get_pos()
        print(x)
        print(y)
        if 22 < x < 74 and 652 < y < 700:
            return 1
        elif 219 < x < 271 and 652 < y < 700:
            return 2
        elif 415 < x < 467 and 652 < y < 700:
            return 3
        elif 612 < x < 664 and 652 < y < 700:
            return 4
        elif 809 < x < 861 and 652 < y < 700:
            return 5
        elif 22 < x < 74 and 702 < y < 750:
            return 6
        elif 219 < x < 271 and 702 < y < 750:
            return 7
        elif 415 < x < 467 and 702 < y < 750:
            return 8
        elif 612 < x < 664 and 702 < y < 750:
            return 9
        elif 809 < x < 861 and 702 < y < 750:
            sys.exit()
        else:
            return 0

    pressed_key = pygame.key.get_pressed()
    if pressed_key[K_0] or pressed_key[K_KP0]:
        sys.exit()
    elif pressed_key[K_1] or pressed_key[K_KP1]:
        return 1
    elif pressed_key[K_2] or pressed_key[K_KP2]:
        return 2
    elif pressed_key[K_3] or pressed_key[K_KP3]:
        return 3
    elif pressed_key[K_4] or pressed_key[K_KP4]:
        return 4
    elif pressed_key[K_5] or pressed_key[K_KP5]:
        return 5
    elif pressed_key[K_6] or pressed_key[K_KP6]:
        return 6
    elif pressed_key[K_7] or pressed_key[K_KP7]:
        return 7
    elif pressed_key[K_8] or pressed_key[K_KP8]:
        return 8
    elif pressed_key[K_9] or pressed_key[K_KP9]:
        return 9
    else:
        return 0


def line():
    """
    メニュー部分のレイアウト作画とメニューの処理
    メニューの文字は8文字まで
    returns: int

    """
    # メニュー文字のレンダリング
    menu1_wd = font_20.render(mwd1, True, (255, 255, 255))
    menu2_wd = font_20.render(mwd2, True, (255, 255, 255))
    menu3_wd = font_20.render(mwd3, True, (255, 255, 255))
    menu4_wd = font_20.render(mwd4, True, (255, 255, 255))
    menu5_wd = font_20.render(mwd5, True, (255, 255, 255))
    menu6_wd = font_20.render(mwd6, True, (255, 255, 255))
    menu7_wd = font_20.render(mwd7, True, (255, 255, 255))
    menu8_wd = font_20.render(mwd8, True, (255, 255, 255))
    menu9_wd = font_20.render(mwd9, True, (255, 255, 255))
    menu0_wd = font_20.render(mwd0, True, (255, 255, 255))
    # メニュー場所初期化
    screen.blit(DBG, (0,650))
    # メニュー文字の表記
    screen.blit(menu1_wd, (76, 666))
    screen.blit(menu2_wd, (273, 666))
    screen.blit(menu3_wd, (470, 666))
    screen.blit(menu4_wd, (667, 666))
    screen.blit(menu5_wd, (864, 666))
    screen.blit(menu6_wd, (76, 716))
    screen.blit(menu7_wd, (273, 716))
    screen.blit(menu8_wd, (470, 716))
    screen.blit(menu9_wd, (667, 716))
    screen.blit(menu0_wd, (864, 716))
    # メニューの枠線
    pygame.draw.rect(screen, (255, 255, 255), Rect(20, 650, 984, 100), 2)
    pygame.draw.line(screen, (255, 255, 255), (20, 700), (1004, 700), 2)
    pygame.draw.line(screen, (255, 255, 255), (217, 650), (217, 750), 2)
    pygame.draw.line(screen, (255, 255, 255), (414, 650), (414, 750), 2)
    pygame.draw.line(screen, (255, 255, 255), (611, 650), (611, 750), 2)
    pygame.draw.line(screen, (255, 255, 255), (808, 650), (808, 750), 2)
    # メニューの数字画像
    screen.blit(M1, (23, 653))
    screen.blit(M2, (220, 653))
    screen.blit(M3, (417, 653))
    screen.blit(M4, (614, 653))
    screen.blit(M5, (811, 653))
    screen.blit(M6, (23, 703))
    screen.blit(M7, (220, 703))
    screen.blit(M8, (417, 703))
    screen.blit(M9, (614, 703))
    screen.blit(M0, (811, 703))


def advance():
    """
    文字を進めるためのwait
    :return: 
    """
    while True:
        ope_num = operation()
        if ope_num == 5:
            break


def dice():
    """
    サイコロの値を返す
    :return: int
    """
    return (random.randint(1, 601) % 6) + 1


def d_wait():
    """
    サイコロのwait
    :return: 
    """
    while True:
        ope_num = operation()
        if ope_num == 6:
            break

"""-----

ウィンドウ作成

-----"""

# 画面解像度
SCREEN_SIZE = (1024, 768)
screen = pygame.display.set_mode(SCREEN_SIZE)

# ウィンドウタイトル
pygame.display.set_caption("やる夫が地下に潜るようです")

"""-----

画像処理

-----"""

# 背景
BG = pygame.image.load(bg).convert()
DBG = pygame.image.load(down).convert()
STBG = pygame.image.load(stat).convert()
# メニュー数字
M1 = pygame.image.load(menu_1).convert()
M2 = pygame.image.load(menu_2).convert()
M3 = pygame.image.load(menu_3).convert()
M4 = pygame.image.load(menu_4).convert()
M5 = pygame.image.load(menu_5).convert()
M6 = pygame.image.load(menu_6).convert()
M7 = pygame.image.load(menu_7).convert()
M8 = pygame.image.load(menu_8).convert()
M9 = pygame.image.load(menu_9).convert()
M0 = pygame.image.load(menu_0).convert()
# タイトル顔
YAR = pygame.image.load(yaruo).convert()

"""-----


ここからゲームループ


-----"""

"""-----

タイトル画面作画

-----"""

while True:

    mwd1 = "　　新規作成　　"
    mwd2 = "　　続きから　　"
    mwd3 = ""
    mwd4 = ""
    mwd5 = ""
    mwd6 = ""
    mwd7 = ""
    mwd8 = ""
    mwd9 = ""
    mwd0 = "　　終了する　　"

    ope_num = operation()

    # 画面表示
    screen.blit(BG, (0, 0))
    line()
    pygame.display.update()

