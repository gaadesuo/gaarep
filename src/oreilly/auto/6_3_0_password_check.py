#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/09 13:49'

import sys
import pyperclip

PASSWORD = {"email": "eqwertyui",
            "blog": "bqwertyui",
            "luggage": "lqwertyui"}


def main():

    print("使い方: python 6_3_0_password_check.py [gaa]")
    print("パスワードをクリップボードにコピーします")
    account = input()

    if account in PASSWORD.keys():
        pyperclip.copy(PASSWORD[account])
        print("{} のパスワードをコピーしました".format(account))
    else:
        print("{} というアカウントは存在しません".format(account))
    sys.exit()


if __name__ == '__main__':
    main()