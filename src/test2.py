
for lpy in range(2, 10):
    print("{0}  ".format(lpy), end="")
    for lpx in range(2, 10):
        print("{0:2d} ".format(lpx*lpy), end="")
    print("")

    # データ入力
    ans = {}
    win = {}
    num_list = []
    lp_num = int(input())
    # 対戦数の計算
    vs_num = int((lp_num - 1) * lp_num / 2)

    # 勝敗検索
    # 全敗の場合リストが作成されないのであらかじめ選手全員のリストを作成
    for lp2 in range(lp_num):
        win[lp2 + 1] = []
    for lp0 in range(vs_num):
        inp_num = [int(lp1) for lp1 in input().split()]
        # print(inp_num)
        win[inp_num[0]].append(inp_num[1])
        # リストの要素をソート
        win[inp_num[0]].sort()
    # print(win)

    # 勝敗表の作成
    for lp3 in range(lp_num):
        ans[lp3 + 1] = []
    for key, num in win.items():
        # print(key, num)
        for lp3 in range(lp_num):
            # print(lp3 + 1)
            if lp3 + 1 == key:
                ans[lp3 + 1].append("-")
            elif lp3 + 1 in num:
                ans[lp3 + 1].append("L")
            else:
                ans[lp3 + 1].append("W")
    # print(ans)

    # 表示
    for non, ans in ans.items():
        print(" ".join(ans))