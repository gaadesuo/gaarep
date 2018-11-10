#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/10 09:58'

import pyperclip


def main():
    new_list = []
    word = pyperclip.paste()
    # print(word)
    word_list = word.split("\n")
    # print(word_list)
    for s in word_list:
        new_list.append("* " + s)
    # print(new_list)
    new_word = "\n".join(new_list)
    pyperclip.copy(new_word)


if __name__ == '__main__':
    main()