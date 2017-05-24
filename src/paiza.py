# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/05/07 :20:46$'


def main():
    pass


if __name__ == '__main__':
    main()

    # paiza D005 等差数列
    n, m = [int(i) for i in input().split()]
    list = []
    for num in range(n, m + (n * 10), m):
        list.append(num)
    list2 = map(str, list)
    print(" ".join(list2))

    # paiza暗号化複合化
    ans_list = []
    nums = input().split()
    keys = [str(key) for key in range(10)]
    enc_dict = {k: n for k, n in zip(keys, nums)}
    word = input()
    c_num = [num for num in input()]
    if word.startswith("enc"):
        ans_list = [enc_dict[i] for i in c_num]
        print("".join(ans_list))
    else:
        for i in c_num:
            for ans_key, ans_val in enc_dict.items():
                if i == ans_val:
                    ans_list.append(ans_key)
    print("".join(ans_list))