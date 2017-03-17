# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "gaa"
__date__ = '$2017/03/11 :05:43$'

import pygame
from pygame.locals import *
import sys
import time

pygame.init()

# -----テキストファイルの設定-----

mona = r'c:\windows\fonts\ipagp-mona.ttf'

# -----画像ファイルの設定-----

yaruo = r"C:\Users\user\Documents\NetBeansProjects\gaarep\PythonProject\yaruo\AA.png"
bg = r"C:\Users\user\Documents\NetBeansProjects\gaarep\PythonProject\yaruo\BG.png"


# -----関数-----

def inp_menu():
    """
    キーボードの入力受け付けとウィンドウからのイベント受け付け
    0もしくはウィンドウの×でプログラム終了
    1～9の入力で各々の数字を返す
    :return: int
    """
    for event in pygame.event.get():
        # 終了イベントが発生したら終了する
        if event.type == QUIT:
            sys.exit()
            # キー入力なら各々の値、0なら終了
    pressed_key = pygame.key.get_pressed()
    if pressed_key[K_0] or pressed_key[K_KP0]:
        sys.exit()
    elif pressed_key[K_1] or pressed_key[K_KP1]:
        return (1)
    elif pressed_key[K_2] or pressed_key[K_KP2]:
        return (2)
    elif pressed_key[K_3] or pressed_key[K_KP3]:
        return (3)
    elif pressed_key[K_4] or pressed_key[K_KP4]:
        return (4)
    elif pressed_key[K_5] or pressed_key[K_KP5]:
        return (5)
    elif pressed_key[K_6] or pressed_key[K_KP6]:
        return (6)
    elif pressed_key[K_7] or pressed_key[K_KP7]:
        return (7)
    elif pressed_key[K_8] or pressed_key[K_KP8]:
        return (8)
    elif pressed_key[K_9] or pressed_key[K_KP9]:
        return (9)


# -----ウィンドウ作成-----

# 画面解像度
SCREEN_SIZE = (1024, 768)
screen = pygame.display.set_mode(SCREEN_SIZE)
# ウィンドウタイトル
pygame.display.set_caption("やる夫が地下に潜るようです")

# フォントの設定
MY_font = pygame.font.Font(mona, 50)
DOR_font = pygame.font.Font(mona, 100)
DOR_font_B = pygame.font.Font(mona, 100)
NAME_font = pygame.font.Font(mona, 40)
MENU_font = pygame.font.Font(mona, 25)

TITLE_NAME_U = DOR_font.render("やる夫が", True, (255, 255, 255))
TITLE_NAME_M = DOR_font.render("地下に", True, (255, 255, 255))
TITLE_NAME_D = DOR_font_B.render("潜るようです", True, (255, 255, 255))
SUB_TITLE = MY_font.render(u"樹海に魅入られし者", True, (255, 255, 255))
M_NAME = NAME_font.render(u"著：がー", True, (255, 255, 255))
T_MENU = MENU_font.render(u"新しく始める:1    続きから:2    終了する:0", \
                          True, (255, 255, 255))

# -----画像の設定-----

BG = pygame.image.load(bg).convert()
YAR = pygame.image.load(yaruo).convert()
# 以下背景を透明化、現在は必要ない
# colorkey = yar.get_at((0,0))
# yar.set_colorkey(colorkey, RLEACCEL)


# -----ゲームループ-----

while True:

    screen.blit(BG, (0,0))
    screen.blit(TITLE_NAME_U, (40, 20))
    screen.blit(TITLE_NAME_M, (300, 150))
    screen.blit(TITLE_NAME_D, (450, 260))
    screen.blit(SUB_TITLE, (500, 400))
    screen.blit(M_NAME, (40, 500))
    screen.blit(T_MENU, (280, 650))
    screen.blit(YAR, (750, 50))

    pygame.display.update()

    menu_num = inp_menu()
    if menu_num == 1:
        break
print("END")
