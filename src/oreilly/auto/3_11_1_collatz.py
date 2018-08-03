# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/08/04 02:24'


def collatz(number):
    """
    コラッツ数列
    :param number: 入力した数字
    :return: 計算した答え
    """
    num = int(number / 2 if number % 2 == 0 else 3 * number + 1)
    return num


def main():
    try:
        num = int(input("整数を入力 >>> "))
        while num != 1:
            num = collatz(num)
            print(num)
    except ValueError:
        print("整数を入れてください")


if __name__ == '__main__':
    main()
