# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/11 :18:36$'

# 辞書の中にキーと集合を入れる
neler = {
        "vipper": {"やる夫", "やらない夫", "できる夫"},
        "nyusoku": {"やる夫", "できる夫", "やる実", "できる子"},
        "women": {"やる実", "やらない子","できる子"},
        "nanJ": {"やきう", "原住民", "やらない夫", "やらない子"}}

print([ita for ita, name in neler.items() if "やる夫" not in name])