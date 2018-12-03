#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/12/01 20:32'

# 入力
ip_list = []
try:
    with open("C005", "r", encoding="UTF-8") as inp_txt:
        for txt in inp_txt:
            ip_list.append(txt.strip())
        inp_txt.close()
        del ip_list[0]

except FileNotFoundError:
    for i in range(int(input())):
        ip_list.append(input())

# print(ip_list)

# 処理
for ip in ip_list:
    ip_num = ip.split(".")
    # print(ip_num)
    try:
        num_list = [int(i) for i in ip_num]
        if len(num_list) != 4:
            print("False")
        else:
            for num in num_list:
                # print(num)
                if num > 255 or num < 0:
                    print("False")
                    break
            else:
                print("True")
    except ValueError:
        print("False")
