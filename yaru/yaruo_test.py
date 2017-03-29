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
nomal = r"C:\Users\user\Documents\NetBeansProjects\gaarep\PythonProject\yaru\image\nomal.png"

"""-----

フォントの設定

-----"""

font_100 = pygame.font.Font(mona, 100)
font_50 = pygame.font.Font(mona, 50)
font_40 = pygame.font.Font(mona, 40)
font_20 = pygame.font.Font(mona, 20)

"""

アイテムデーター

"""

# 武器
wep_0 = [u"なし",0]
wep_1 = [u"ブロードソード",5]
weapon = {0:wep_0, 1: wep_1}

# 盾
shie_0 = [u"なし",0]
shie_1 = [u"レザーシールド",1]
shield = {0:shie_0, 1: shie_1}

# 兜
hel_0 = [u"なし",0]
hel_1 = [u"レザーヘルメット",1]
helmet = {0:hel_0, 1: hel_1}

# 鎧
arm_0 = [u"なし",0]
arm_1 = [u"レザーアーマー",1]
armor = {0: arm_0, 1: arm_1}

# 小手
gaunt_0 = [u"なし",0]
gaunt_1 = [u"レザーガントレット",1]
gauntlet = {0: gaunt_0, 1: gaunt_1}

# 具足
leg_0 = [u"なし",0]
leg_1 = [u"レザーアンク",1]
leg_armor = {0: leg_0, 1:leg_1}

# 指輪
ring_0 = [u"なし",0,0]
ring = {0: ring_0}

# ネックレス
neck_0 = [u"なし",0,0]
necklace = {0: neck_0}

# お守り
amu_0 = [u"なし",0,0]
amulet = {0: amu_0}

# アイテム
item_0 = [""]
item_1 = ["ポーション"]


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


def status_windows():
    """
    ステータス画面    
    :return: 
    """
    while True:
        global mwd0
        global mwd1
        global mwd2
        global mwd3
        global mwd4
        global mwd5
        global mwd6
        global mwd7
        global mwd8
        global mwd9
        mwd1 = ""
        mwd2 = ""
        mwd3 = ""
        mwd4 = ""
        mwd5 = ""
        mwd6 = ""
        mwd7 = ""
        mwd8 = ""
        mwd9 = ""
        mwd0 = "　　終了する　　"

        ope_num = operation()

        # 文字レンダリング
        STAT_LV = font_20.render("LV    {0:3d}".format(LV), True, (255, 255, 255))
        STAT_HP = font_20.render("HP/MHP  {}/{}".format(HP, MHP), True, (255, 255, 255))
        STAT_STR = font_20.render("STR   {0:3d}".format(STR), True, (255, 255, 255))
        STAT_VIT = font_20.render("VIT   {0:3d}".format(VIT), True, (255, 255, 255))
        STAT_AGI = font_20.render("AGI   {0:3d}".format(AGI), True, (255, 255, 255))
        STAT_EXP = font_20.render("EXP   {}".format(EXP), True, (255, 255, 255))
        STAT_WEP = font_20.render("{}".format(R_ARM[0]), True, (255, 255, 255))
        STAT_SHIE = font_20.render("{}".format(L_ARM[0]), True, (255, 255, 255))
        STAT_HEL = font_20.render("{}".format(HEAD[0]), True, (255, 255, 255))
        STAT_ARM = font_20.render("{}".format(BODY[0]), True, (255, 255, 255))
        STAT_GAUN = font_20.render("{}".format(HAND[0]), True, (255, 255, 255))
        STAT_LEG = font_20.render("{}".format(FOOT[0]), True, (255, 255, 255))
        STAT_RING = font_20.render("{}".format(RING[0]), True, (255, 255, 255))
        STAT_NECK = font_20.render("{}".format(NECK[0]), True, (255, 255, 255))
        STAT_AMUL = font_20.render("{}".format(AMUL[0]), True, (255, 255, 255))
        STAT_E_DEF = font_50.render("{0:3d}".format(E_DEF), True, (255, 255, 255))
        STAT_E_ATT = font_50.render("{0:3d}".format(E_ATT), True, (255, 255, 255))
        STAT_DEF = font_50.render("{0:3d}".format(DEF), True, (255, 255, 255))
        STAT_ATT = font_50.render("{0:3d}".format(ATTACK), True, (255, 255, 255))

        # 画面表示
        screen.blit(STBG, (0, 0))
        screen.blit(STAT_LV, (646, 40))
        screen.blit(STAT_HP, (640, 70))
        screen.blit(STAT_STR, (640, 100))
        screen.blit(STAT_VIT, (647, 130))
        screen.blit(STAT_AGI, (645, 160))
        screen.blit(STAT_EXP, (642, 200))
        screen.blit(NOR, (800, 50))
        screen.blit(STAT_WEP, (360, 356))
        screen.blit(STAT_SHIE, (360, 70))
        screen.blit(STAT_HEL, (360, 100))
        screen.blit(STAT_ARM, (360, 130))
        screen.blit(STAT_GAUN, (360, 160))
        screen.blit(STAT_LEG, (360, 190))
        screen.blit(STAT_E_DEF, (203, 111))
        screen.blit(STAT_E_ATT, (203, 340))
        screen.blit(STAT_DEF, (58, 111))
        screen.blit(STAT_ATT, (58, 340))
        screen.blit(STAT_RING, (48, 548))
        screen.blit(STAT_NECK, (248, 548))
        screen.blit(STAT_AMUL, (446, 548))
        line()

        pygame.display.update()

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
# ステータス顔
NOR = pygame.image.load(nomal).convert()

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

    # 文字レンダリング
    TITLE_NAME_U = font_100.render("やる夫が", True, (255, 255, 255))
    TITLE_NAME_M = font_100.render("地下に", True, (255, 255, 255))
    TITLE_NAME_D = font_100.render("潜るようです", True, (255, 255, 255))
    SUB_TITLE = font_50.render(u"樹海に魅せられし者", True, (255, 255, 255))
    M_NAME = font_40.render(u"著：がー", True, (255, 255, 255))

    # 画面表示
    screen.blit(BG, (0, 0))
    screen.blit(TITLE_NAME_U, (40, 20))
    screen.blit(TITLE_NAME_M, (300, 150))
    screen.blit(TITLE_NAME_D, (450, 260))
    screen.blit(SUB_TITLE, (500, 400))
    screen.blit(M_NAME, (40, 500))
    screen.blit(YAR, (690, 0))
    line()
    pygame.display.update()

    if ope_num == 1:
        break
    elif ope_num == 2:
        conti.con()
    else:
        pass

"""------

エピローグ

-----"""

while True:

    mwd1 = ""
    mwd2 = ""
    mwd5 = "　文章を進める　"

    ope_num = operation()

    # レンダリング
    WDS_1 = font_20.render \
        (u"とある町の外れにある樹海。そこでもたらされる恵みは、その町の支えの一つであった。" \
         , True, (255, 255, 255))
    WDS_2 = font_20.render \
        (u"ある日、その樹海から謎の生物を見かけるようになる。そして、それは人々に対し攻撃的であった。" \
         , True, (255, 255, 255))
    WDS_3 = font_20.render \
        (u"そして生まれる、弱肉強食の世界。不自由なく得られた恵みは、弱者にとっては手の届かぬものになってしまう。" \
         , True, (255, 255, 255))
    WDS_4 = font_20.render \
        (u"それを解決するべく、国は報奨金を出して世界中から猛者を募った。" \
         , True, (255, 255, 255))
    WDS_5 = font_20.render \
        (u"ならず者は吼えた。我こそが栄光を掴む！と。" \
         , True, (255, 255, 255))
    WDS_6 = font_20.render \
        (u"術師はほくそ笑んだ。修行の成果を試すときだ。と" \
         , True, (255, 255, 255))
    WDS_7 = font_20.render \
        (u"騎士は誓った。皆の望みをかなえてやる。と。" \
         , True, (255, 255, 255))
    WSD_8 = font_20.render \
        (u"一人。そして、また一人。次々に挑んではいくが、しばらくすると同じ人を見かけなくなる。" \
         , True, (255, 255, 255))
    WSD_9 = font_20.render \
        (u"不安と混沌が渦巻く地方。そこに今、あなたはたどり着いたばかりだった" \
         , True, (255, 255, 255))
    WSD_10 = font_20.render \
        (u"あなたもこの樹海に魅せられた者の一人だ。さぁ、ひるまずに立ち向かいたまえ！" \
         , True, (255, 255, 255))

    WDS = [WDS_1, WDS_2, WDS_3, WDS_4, WDS_5, WDS_6, WDS_7, WSD_8, WSD_9]

    # 画面表示
    screen.blit(BG, (0, 0))
    line()
    n = 0
    for lp_0 in range(9):
        n += 1
        screen.blit(WDS[n - 1], (40, (20 + (40 * n))))
        pygame.display.update()
        time.sleep(0.5)
        advance()
    mwd5 = "　キャラ作成へ　"
    line()
    screen.blit(WSD_10, (120, 500))
    pygame.display.update()
    time.sleep(0.5)
    advance()
    break

"""-----

キャラメイク

-----"""

while True:
    mwd5 = ""
    mwd6 = "　ダイスを振る　"
    mwd7 = ""
    mwd8 = ""
    n = 0
    flg = 0
    ope_num = operation()
    status = []
    for lp_1 in range(5):
        status.append(dice())

    # レンダリング
    WDS_1 = font_20.render(u"＊ キャラクター作成 ＊", True, (255, 255, 255))
    WDS_2 = font_20.render(u"能力値を決定させるため、ダイスを5回振ります。" \
                           , True, (255, 255, 255))
    WDS_3 = font_20.render("{}".format(status[0]),True, (255, 255, 255))
    WDS_4 = font_20.render("{}".format(status[1]), True, (255, 255, 255))
    WDS_5 = font_20.render("{}".format(status[2]), True, (255, 255, 255))
    WDS_6 = font_20.render("{}".format(status[3]), True, (255, 255, 255))
    WDS_7 = font_20.render("{}".format(status[4]), True, (255, 255, 255))
    WDS_8 = font_20.render(">>>", True, (255, 255, 255))
    WDS_9 = font_20.render(u"以上でよろしいですか？", True, (255, 255, 255))
    WDS_10 = font_20.render(u"キャラクターを作成します。", True, (255, 255, 255))
    WDS_CM = [WDS_3, WDS_4, WDS_5, WDS_6, WDS_7]

    # 画像表示
    screen.blit(BG, (0, 0))
    screen.blit(WDS_1, (40, 20))
    screen.blit(WDS_2, (40, 60))
    line()
    pygame.display.update()
    for lp_2 in range(5):
        n += 1
        screen.blit(WDS_8, (40, (60 + (40 * n))))
        pygame.display.update()
        d_wait()
        screen.blit(WDS_CM[n - 1], (80, (60 + (40 * n))))
        pygame.display.update()
        time.sleep(0.5)

    mwd6 = ""
    mwd7 = "　　　はい　　　"
    mwd8 = "　　　いいえ　　"
    line()
    screen.blit(WDS_9, (40, 300))
    pygame.display.update()

    while flg == 0:
        ope_num = operation()
        if ope_num == 7:
            break
        elif ope_num == 8:
            flg = 1
    else:
        continue

    mwd5 = "　ステータスへ　"
    mwd7 = ""
    mwd8 = ""
    line()
    screen.blit(WDS_10, (40, 340))
    pygame.display.update()

    # キャラステータス作成
    LV = 1
    STR = (6 + status[0]) // 2
    VIT = (6 + status[1]) // 2
    AGI = (6 + status[2]) // 2
    MHP = (10 + ((status[3] + status[4]) // 2))
    HP = MHP
    EXP = 0
    R_ARM = weapon[1]
    L_ARM = shield[1]
    HEAD = helmet[1]
    BODY = armor[1]
    HAND = gauntlet[1]
    FOOT = leg_armor[1]
    RING = ring[0]
    NECK = necklace[0]
    AMUL = amulet[0]

    E_DEF = L_ARM[1] + HEAD[1] + BODY[1] + HAND[1] + FOOT[1] + RING[2] + NECK[2] + AMUL[2]
    E_ATT = R_ARM[1] + RING[1] + NECK[1] + AMUL[1]
    DEF = E_DEF + VIT
    ATTACK = E_ATT + STR

    while True:
        ope_num = operation()
        if ope_num == 5:
            break

    status_windows()
