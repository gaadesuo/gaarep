# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/08/04 09:27'


def comma(w_list):
    """
    単語のリストの要素をカンマでつないで最後の前にandを入れる文字列を返す
    :param w_list: 単語のリスト
    return: 文字列
    """
    for i in w_list[:-1]:
        print(i, end=", ")
    print("and " + w_list[-1])


def main():
    spam = ["apples", "bananas", "tofu", "cats"]
    comma(spam)


if __name__ == '__main__':
    main()
