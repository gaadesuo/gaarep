# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/02 :20:36$'

import PIN14_15_LED as LED

# ２回繰り返して終わりを表示して終了
for lp1 in range(2):
    LED.led14(5)
    LED.led15(5)
    LED.led14and15(5)

print (u"終わり")
