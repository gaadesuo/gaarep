#! /usr/bin/python
# :-*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "user"
__date__ = "$2017/02/24 19:10:13$"

import wiringpi as GPIO
from time import sleep

# -----GPIOセットアップ-----

buzzer = 26  # 左19

GPIO.wiringPiSetupGpio()
GPIO.softToneCreate(buzzer)

# -----音階周波数-----
lsi = 247
do = 262
re = 294
mi = 330
fa = 349
so = 392
ra = 440
si = 494
hdo = 523
morse = 815

# -----楽譜date-----
onpu = (re, re, do, lsi, re, so, ra, si, si, si, ra, so, mi, mi, mi, fa, so, fa,\
        so, mi, re, mi, re, lsi, re, re, re, re, do,lsi, re, so, ra, si, si, si,\
        ra, so, ra, ra, ra, ra, so, so, fa, fa, so, so, so)
mtime = (4, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1,\
         1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1,\
         1)
stime = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\
         8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4,\
         4)

if __name__ == "__main__":

    # -----演奏-----

    for (yodo, mero, stp) in zip(onpu, mtime, stime):
        GPIO.softToneWrite(buzzer, yodo)
        sleep(mero / 10)
        GPIO.softToneWrite(buzzer, 0)
        sleep(stp / 10)
