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

    ans_list2 = []
    num = int(input())
    up_list = [int(i) for i in input().split()]
    low_list = [int(i) for i in input().split()]

    for m in range(num):
        ans_list = []
        for n in range(num):
            ans = low_list[m] + up_list[n]
            ans_list.append(str(ans))
        ans_list2.append(ans_list)

    for o in range(num):
        print(" ".join(ans_list2[o]))

    # その２

    p_list = []
    b_list = []
    # キャンペーン商品数と割引設定入力

    # 入力される値は割引商品の種類数
    for lp0 in range(int(input())):
        # 入力される値は[0]から単価 割引される個数 割引額
        price = [int(lp1) for lp1 in input().split()]
        # print(price)
        p_list.append(price)
    # print(p_list)

    # 購入種類と数の入力

    # 入力される値は購入種類数
    for lp2 in range(int(input())):
        # 入力される値は[0]から製品NO 購入数
        buy = [int(lp3) for lp3 in input().split()]
        # print(buy)
        b_list.append(buy)
    # print(b_list)

    # 処理

    for lp4 in range(lp2 + 1):
        kind = (b_list[lp4][0] - 1)
        discount = b_list[lp4][1] / p_list[kind][1]
        if 0 < int(discount):
            print((p_list[kind][0] * b_list[lp4][1]) - (p_list[kind][2] * int(discount)))
        else:
            print(p_list[kind][0] * b_list[lp4][1])

    # その３
    hi_list = ["200"]
    low_list = ["100"]
    for lp1 in range(int(input())):
        high = input().split()
        hi_list.append(high[1]) if high[0] == "le" else low_list.append(high[1])
    print("{} {}".format(max(low_list), min(hi_list)))