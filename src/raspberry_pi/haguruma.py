# -*- coding: utf-8 -*-
# ***データ入力***
date_dic = {}
for lp0 in range(int(input())):
    inp_date = input().split()
    # print("入力されたデータは" + str(inp_date))

    # ***処理***
    if int(inp_date[0]) in date_dic:
        date_dic[int(inp_date[0])] += inp_date[1]
    else:
        date_dic[int(inp_date[0])] = inp_date[1]

# ***表示***
for key, val in date_dic.items():
    print("{:0d} {}".format(key, val))