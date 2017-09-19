# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/05/07 :20:46$'


def main():
    pass


if __name__ == '__main__':
    main()

    """
    
    C043 使用回数の調査
    
    """

    import collections

    # データーの入力
    count_num = int(input())
    inp_num = [int(lp0) for lp0 in input().split()]
    print(inp_num)

    # 入力値を要素別にまとめる
    # 対象リストの要素を要素別にカウントをしてキーでソートする
    ans_dict = collections.Counter(inp_num)
    print(ans_dict)
    # 辞書の値の最大値を求める
    max_num = max(ans_dict.values())
    print(max_num)

    # 最大値の値のkeyを抜き出す
    ans_list = []
    for key, val in ans_dict.items():
        if val == max_num:
            ans_list.append(key)
    print(ans_list)
    ans_list = sorted(ans_list, key=int)
    ans_list = [str(lp1) for lp1 in ans_list]

    # 表示
    print(" ".join(ans_list))

    """
    
    C042 リーグ表の作成
    
    """

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

    """
    
    C041 メダルランキングの作成
    
    """

    # データ入力
    medals = []
    for lp0 in range(int(input())):
        inp_list = [int(lp1) for lp1 in input().split()]
        medals.append(inp_list)
    # print(medals)

    ans_list = sorted(medals, reverse=True)
    for lp2 in ans_list:
        print("{} {} {}".format(lp2[0], lp2[1], lp2[2]))

    """
    
    C040 背比べ
    
    """

    hi_list = ["200"]
    low_list = ["100"]
    for lp1 in range(int(input())):
        high = input().split()
        hi_list.append(high[1]) if high[0] == "le" else low_list.append(high[1])
    print("{} {}".format(max(low_list), min(hi_list)))

    """
    
    C039 古代の数式
    
    """

    word = input()
    # print(word)
    ten = word.count("<")
    one = word.count("/")
    print((ten * 10) + one)

    """
    
    C038 お菓子の配分
    
    """

    # データ入力
    inp_num = [int(lp0) for lp0 in input().split()]
    # print("機械の数とお菓子の数")
    # print(inp_num)

    # 機械ごとの箱の数の入力と計算
    box = []
    ans = []
    index = []
    for lp0 in range(inp_num[0]):
        box.append(int(input()))
        ans.append(inp_num[1] % box[lp0])
    # print(box)
    # print(ans)

    # あまりが最小の機械のインデックスの検索
    ans_list = []
    c_num = 0
    for lp1 in ans:
        if lp1 == min(ans):
            index.append(c_num)

        c_num += 1
    # print(index)
    for lp2 in index:
        ans_list.append(box[lp2])
    # print(ans_list)

    # 表示
    print((box.index(max(ans_list))) + 1)

    # あっこさんの

    amari = []
    hako = []
    n = 0

    # 入力は 機械の数 お菓子の数
    okasi = [int(lp0) for lp0 in input().split()]

    for lp1 in range(okasi[0]):
        wari = int(input())
        kari_amari = okasi[1] % wari
        kari_hako = int(okasi[1] / wari)
        amari.append(okasi[1] % wari)
        hako.append(int(okasi[1] / wari))
        # print(amari, hako)

        if n == 0:
            ans = wari
        else:
            if kari_amari >= min(amari):
                if kari_hako > max(hako):
                    ans = wari

            else:
                ans = wari
        n += 1
    print(ans)

    """
    
    C037 アニメの日時
    
    """

    # データー入力
    day_time = input().split()
    # print(day_time)
    day_date = [int(lp0) for lp0 in day_time[0].split("/")]
    # print(day_date)
    time_date = [int(lp1) for lp1 in day_time[1].split(":")]
    # print(time_date)

    # 処理
    time_plus = int(time_date[0] / 24)
    # print(time_plus)
    print("{:02d}/{:02d} {:02d}:{:02d}".format(day_date[0], day_date[1] + time_plus, time_date[0] - (24 * time_plus),
                                               time_date[1]))

    """
    
    C036 犬ぞりレース
    
    """

    # データ入
    vs_1_1 = [int(lp0) for lp0 in input().split()]
    vs_1_2 = [int(lp1) for lp1 in input().split()]
    # print("1開戦")
    # print(vs_1_1, vs_1_2)
    time_1 = [int(lp2) for lp2 in input().split()]
    time_2 = [int(lp3) for lp3 in input().split()]
    # print("一回戦時間")
    # print(time_1)
    # print("二回戦時間")
    # print(time_2)

    # 勝利判定1回戦の2戦目
    if time_1[vs_1_1[0] - 1] < time_1[vs_1_1[1] - 1]:
        win_1_point = time_1[vs_1_1[0] - 1]
    else:
        win_1_point = time_1[vs_1_1[1] - 1]

    win1 = time_1.index(win_1_point) + 1

    # print("勝者: " + str(win1))

    # 勝利判定1回戦の2戦目
    if time_1[vs_1_2[0] - 1] < time_1[vs_1_2[1] - 1]:
        win_2_point = time_1[vs_1_2[0] - 1]
    else:
        win_2_point = time_1[vs_1_2[1] - 1]

    win2 = time_1.index(win_2_point) + 1

    # print("勝者: " + str(win2))

    vs_2 = [win1, win2]
    # print("2回戦")
    # print(vs_2)

    if time_2[0] < time_2[1]:
        print(min(vs_2))
        print(max(vs_2))
    else:
        print(max(vs_2))
        print(min(vs_2))

    """
    
    C035 試験の合格判定
    
    """

    # データ入力
    ans = 0
    inp_num = int(input())
    for lp0 in range(inp_num):
        date_list = input().split()
        # print(date_list)

        # 結果判定
        point_num = 0
        if date_list[0] == "l":
            del date_list[0]
            if int(date_list[-1]) + int(date_list[-2]) >= 160:
                for lp2 in date_list:
                    point_num += int(lp2)
                # print(point_num)
                if point_num >= 350:
                    ans += 1

        elif date_list[0] == "s":
            del date_list[0]
            if int(date_list[1]) + int(date_list[2]) >= 160:
                for lp2 in date_list:
                    point_num += int(lp2)
                # print(point_num)
                if point_num >= 350:
                    ans += 1

    print(ans)

    """
    
    C034 先生の宿題
    
    """

    # データ入力
    inp_num = [lp0 for lp0 in input().split()]
    # print(inp_num)

    # Xがどこにあるか検索
    ind_num = inp_num.index("x")
    # print(ind_num)

    # 処理
    if inp_num[1] == "+":
        if ind_num == 0:
            print(int(inp_num[4]) - int(inp_num[2]))
        elif ind_num == 2:
            print(int(inp_num[4]) - int(inp_num[0]))
        else:
            print(int(inp_num[0]) + int(inp_num[2]))

    else:
        if ind_num == 0:
            print(int(inp_num[4]) + int(inp_num[2]))
        elif ind_num == 2:
            print(int(inp_num[0]) - int(inp_num[4]))
        else:
            print(int(inp_num[0]) - int(inp_num[2]))

    """
    
    C033 やきうの審判
    
    """

    # データーの入力
    strike_count = 0
    ball_count = 0
    inp_num = int(input())
    for lp0 in range(inp_num):
        nanJ = input()
        if nanJ == "ball":
            ball_count += 1
            print("ball!" if ball_count < 4 else "fourball!")
        elif nanJ == "strike":
            strike_count += 1
            print("strike!" if strike_count < 3 else "out!")

    """
    
    C32 お得なお買い物
    
    """

    # データーの入力
    point = 0
    a_payment = 0
    b_payment = 0
    c_payment = 0
    d_payment = 0
    count = int(input())
    for lp0 in range(count):
        date_list = [int(lp1) for lp1 in input().split()]
        # print(date_list)

        # 種類別の買い物の総金額
        if date_list[0] == 0:
            a_payment += date_list[1]
        elif date_list[0] == 1:
            b_payment += date_list[1]
        elif date_list[0] == 2:
            c_payment += date_list[1]
        else:
            d_payment += date_list[1]

    point += int(a_payment / 100) * 5
    point += int(b_payment / 100) * 3
    point += int(c_payment / 100) * 2
    point += int(d_payment / 100)
    print(point)

    """
    
    C031 時差を求めたい
    
    """

    # 70点
    import math

    # 最大で持てる量
    max = int(input())
    # print("最大で持てる量:" +str(max))

    # faxのデーター入力
    fax_list = []
    count = int(input())
    for lp1 in range(count):
        fax = [int(lp2) for lp2 in input().split()]
        fax_list.append(fax)
    # print("fax date list")
    # print(fax_list)

    # データーの処理
    ans = 0
    peper = 0
    # print("時間ごとのfax date")
    for lp3 in range(25):
        for lp4 in fax_list:
            if lp3 == lp4[0]:
                # print(lp3, lp4)
                peper += lp4[2]
                # print("時間ごとの紙の数" + str(peper))
            else:
                ans += math.ceil(peper / max)
                peper = 0

    # 表示
    print(ans)

    """
    
    C030 白にするか黒にするか
    
    """

    # 画面の縦横数[0]:縦 [1]:横
    screen = [int(lp0) for lp0 in input().split()]
    # print("縦:横  " +str(screen))

    ans_list = []
    for lp1 in range(screen[0]):
        color = [int(lp2) for lp2 in input().split()]
        # print(color)
        ans_list = ["1" if lp3 >= 128 else "0" for lp3 in color]
        # print(ans_list)
        print(" ".join(ans_list))

    """
    
    C029 旅行の計画
    
    """

    # 休みと旅行のデータ入力[0]:連休 [1]:旅行の日
    day = [int(lp0) for lp0 in input().split()]
    # print("連休と旅行の日数" + str(day))

    # 連休の日にちと降水確率のデータ入力
    rain_list = []
    for lp1 in range(day[0]):
        rain = [int(lp2) for lp2 in input().split()]
        rain_list.append(rain)
    # print("連休の日にちと降水確率")
    # print(rain_list)

    # 旅行の日程期間の降水確率のデータ集め
    rain_date = 0
    rain_date_list = []
    for lp3 in range(len(rain_list)):
        if lp3 == (len(rain_list) - (day[1] - 1)):
            break
        else:
            for lp4 in range(day[1]):
                rain_date += rain_list[lp3 + lp4][1]

            # rain_date = rain_list[lp3][1] + rain_list[lp3 + 1][1] + rain_list[lp3 + 2][1]
            rain_date_list.append(rain_date)
            rain_date = 0
    # print("各々の旅行期間の降水確率" + str(rain_date_list))

    # 最小値を求める
    trabel = rain_date_list.index(min(rain_date_list))
    # print("最小のインデックスNO: " + str(trabel))

    # 表示
    print("{} {}".format(rain_list[trabel][0], rain_list[trabel + day[1] - 1][0]))

    """
    
    C028 単語テストの採点
    
    """

    # データー入力
    ans = 0
    count = 0
    w_list1 = []
    w_list2 = []
    for lp0 in range(int(input())):
        word = input().split()
        # print(word)
        if len(word[0]) == len(word[1]):
            w_list1 = [lp1 for lp1 in word[0]]
            w_list2 = [lp2 for lp2 in word[1]]
            for lp3 in range(len(word[0])):
                # print(w_list1[lp3], w_list2[lp3])
                if w_list1[lp3] != w_list2[lp3]:
                    count += 1
            # print(count)
            if count == 0:
                ans += 2
            elif count == 1:
                ans += 1
            else:
                ans += 0
            count = 0
    print(ans)

    """
    
    C026 ウサギと人参
    
    """

    # 条件入力
    inp_num = [int(lp0) for lp0 in input().split()]
    # print(inp_num)

    # ニンジンのデーター入力
    food = []
    count = []
    for lp1 in range(inp_num[0]):
        carrot = [int(lp2) for lp2 in input().split()]
        # print(carrot)
        if (inp_num[1] - inp_num[2]) <= carrot[1] <= (inp_num[1] + inp_num[2]):
            food.append(carrot[0])
            count.append(lp1 + 1)
            # print("規定内の重量" + str(food))
            # print("規定内の順番" + str(count))

    # 処理
    # 規定内の人参がなかった時の処理
    if len(food) == 0:
        ans = "not found"
    else:
        big = max(food)
        # print("最大の人参の大きさ  " + str(big))
        cheke = food.count(big)
        # print("最大の人参が何個あるか  " + str(cheke))
        # 人参の最大値が複数時の処理
        if cheke > 1:
            ans = (count[food.index(big)])
        # それ以外は重量の最大値
        else:
            ans = (count[food.index(max(food))])

    print(ans)

    """
    
    C025 ファックスの用紙回収
    
    """

    # 正解
    import math

    # 最大で持てる量
    max = int(input())
    # print("最大で持てる量:" +str(max))

    # faxのデーター入力
    fax_list = []
    count = int(input())
    for lp1 in range(count):
        fax = [int(lp2) for lp2 in input().split()]
        fax_list.append(fax)
    # print("fax date list")
    # print(fax_list)

    # データーの処理
    ans = 0
    peper = 0
    # print("時間ごとのfax date")
    for lp3 in range(25):
        for lp4 in fax_list:
            if lp3 == lp4[0]:
                # print(lp3, lp4)
                peper += lp4[2]
                # print("時間ごとの紙の数" + str(peper))
            else:
                ans += math.ceil(peper / max)
                peper = 0

    # 表示
    print(ans)

    # 不正解
    import math

    # 持てる最大数
    limit = int(input())
    # print(limit)

    # FAXのデーター入力
    count = int(input())
    fax_list = []
    for lp0 in range(count):
        fax = [int(lp1) for lp1 in input().split()]
        fax_list.append(fax)
    # print(fax_list)

    # データー処理
    peper = 0
    for lp2 in range(len(fax_list)):
        try:
            if fax_list[lp2][0] == fax_list[lp2 + 1][0]:
                peper += fax_list[lp2][2]
            else:
                peper += fax_list[lp2][2]
                # print(peper)
                ans = math.ceil(peper / limit)
                # print(ans)
                peper = 0
        except:
            # print(peper + fax_list[-1][2])
            ans += (math.ceil(((peper + fax_list[-1][2]) / limit)))
            print(ans)

    """
    
    C024 ミニコンピュータ
    
    """

    # データーの入力
    count = int(input())
    num1 = 0
    num2 = 0
    for lp0 in range(count):
        command = [lp1 for lp1 in input().split()]
        # print(command)

        # 実行処理
        if command[0] == "SET":
            if command[1] == "1":
                num1 = int(command[2])
                # print("num1  " + str(num1))
            else:
                num2 = int(command[2])
                # print("num2  " + str(num2))
        elif command[0] == "ADD":
            num2 = num1 + int(command[1])
            # print(num2)
        elif command[0] == "SUB":
            num2 = num1 - int(command[1])
            # print(num2)

        else:
            print("適正命令を入れてください")

    # 結果表示
    print(num1, num2)

    """
    
    C023 クジの当選番号
    
    """

    # 当たりの入力
    chance = [int(lp0) for lp0 in input().split()]
    # print(chance)

    # くじの入力
    count = int(input())
    for lp1 in range(count):
        kuji = [int(lp2) for lp2 in input().split()]
        # print(kuji)

        # あたり判定と表示
        hit = 0
        for lp4 in range(len(chance)):
            for lp3 in kuji:
                if chance[lp4] == lp3:
                    hit += 1
        print(hit)
        hit = 0

    """
    
    C022 ローソクの足
    
    """

    # 株価のデーター入力
    count = int(input())
    datelist = []
    for lp0 in range(count):
        date = [int(lp1) for lp1 in input().split()]
        # print(date)
        for lp1 in date:
            datelist.append(lp1)
            # print(datelist)

    # 処理と結果
    print(datelist[0], datelist[-3], max(datelist), min(datelist))

    """
    
    C 021 暴風域にいますか
    
    """

    # 台風のデータ入力と範囲の計算
    circle = [int(lp0) for lp0 in input().split()]
    # print("台風の情報")
    # print(circle)
    anti = circle[2] ** 2
    dang = circle[3] ** 2
    # print("台風の目と暴風圏")
    # print(anti)
    # print(dang)

    # 人数の入力
    men = int(input())

    # 人間の座標入力と台風の判定
    map_list = []
    for lp1 in range(men):
        map = [int(lp2) for lp2 in input().split()]
        # print("人の座標")
        # print(map)
        iti = ((circle[0] - map[0]) ** 2) + ((circle[1] - map[1]) ** 2)
        # print("計算結果")
        # print("iti")
        print("yes" if anti <= iti <= dang else "no")

    """
    
    C 020 残り物の量
    
    """

    # データーの入力
    inp = [int(lp0) for lp0 in input().split()]
    # print(inp)

    # 処理
    if inp[1] == 100:
        print(0)
    else:
        a = inp[0] - (inp[0] * (inp[1] * 0.01))
        b = a - (a * (inp[2] * 0.01))
        print(b)

    """
    
    C 019 完全数とほぼ完全数
    
    """

    # 数字の入力
    for lp0 in range(int(input())):
        num = int(input())
        ans_list = []
        # print("入力された数字")
        # print(num)
        # print("約数")
        for lp1 in range(num):
            # 約数を取得
            if (num % (lp1 + 1)) == 0:
                ans_list.append(lp1 + 1)
        # print(ans_list)

        # 自身を抜いた約数の総和を計算
        ans_num = sum(ans_list) - ans_list[-1]
        # print("自身を抜いた総和")
        # print(ans_num)

        # 結果判定
        if ans_num == num:
            print("perfect")
        elif ans_num == num - 1:
            print("nearly")
        else:
            print("neither")

    """
    
    C 018 何人前作れる？
    
    """
    # 一部結果エラー

    # 必要な食材の種類
    must_num = int(input())

    # 必要な食材データーの入力
    must_food_list = []
    # print("必要な食材と数")
    for lp0 in range(must_num):
        must_food = [lp1 for lp1 in input().split()]
        must_food_list.append(must_food)
    # print(must_food_list)

    # 手持ちの食材の種類
    have = int(input())

    # 手持ちの食材のデーター入力
    # print("手持ちの食材と数")
    have_food_list = []
    for lp2 in range(have):
        have_food = [lp3 for lp3 in input().split()]
        have_food_list.append(have_food)
    # print(have_food_list)

    # 判定
    ans = []
    for lp4 in range(len(must_food_list)):
        # print(lp4)
        for lp5 in range(len(have_food_list)):
            # print(lp5)
            if must_food_list[lp4][0] == have_food_list[lp5][0]:
                # print(must_food_list[lp4][0], have_food_list[lp5][0])
                ans_num = (int(have_food_list[lp5][1]) / int(must_food_list[lp4][1]))
                # print(ans_num)
                ans.append(int(ans_num))
    print("0" if len(ans) == 0 else min(ans))

    """
    
    C 017 ハイアンドロー・カードゲーム
    
    """

    # ***データー入力***
    oya = [int(lp0) for lp0 in input().split()]
    # print("親のカードの一枚目, 二枚目" + str(oya))
    for lp1 in range(int(input())):
        ko = [int(lp2) for lp2 in input().split()]
        # print("子のカードの一枚目, 二枚目" + str(ko))

        # ***処理と表示***
        if oya[0] == ko[0]:
            print("Low" if oya[1] > ko[1] else "High")
        else:
            print("High" if oya[0] > ko[0] else "Low")

    """
    
    C 016 Leet文字列
    
    """

    # ***変換データー用のリスト***
    befoer = ["A", "E", "G", "I", "O", "S", "Z"]
    after = ["4", "3", "6", "1", "0", "5", "2"]

    # ***データー入力***
    inp_word = input()
    # print("入力された文字列は " + str(inp_word))

    # ***変換***
    for (bef_word, aft_word) in zip(befoer, after):
        inp_word = inp_word.replace(bef_word, aft_word)

    # ***表示***
    print(inp_word)

    """
    
    C 015 ポイントカードの計算
    
    """

    # データー入力
    ans = 0
    for lp0 in range(int(input())):
        inp_date = [int(lp1) for lp1 in input().split()]
        # print("レシートのデータ。0:日, 1:￥ " + str(inp_date))

        # 日にち検索用
        day = list(str(inp_date[0]))

        # 判定とポイントの加算
        if day.count("3") > 0:
            ans += int(inp_date[1] * 0.03)
        elif day.count("5") > 0:
            ans += int(inp_date[1] * 0.05)
        else:
            ans += int(inp_date[1] * 0.01)

    # 表示
    print(ans)

    """
    
    C 014 ボールが入る箱
    
    """

    import numpy as np

    # データ入力
    inp_num = [int(lp0) for lp0 in input().split()]
    # print("箱の種類, 球の半径" + str(inp_num))
    for lp1 in range(inp_num[0]):
        box = [int(lp2) for lp2 in input().split()]
        # print("箱の縦, 横, 高さ" + str(box))

        # ***判定***
        np_box = np.array(box)
        if (np_box >= (inp_num[1] * 2)).all():
            print(lp1 + 1)

    """
    
    C 013 嫌いな数字
    
    """

    # ***データー入力***
    ans_list = []
    non_num = input()
    # print("嫌いな数字は" + str(non_num))
    for lp0 in range(int(input())):
        room_no = input()
        # print("部屋番号は " + str(room_no))

        # ***判定***
        no_list = list(room_no)
        if no_list.count(non_num) == 0:
            ans_list.append(room_no)

    # ***表示***
    if len(ans_list) == 0:
        print("none")
    else:
        for lp1 in ans_list:

    """
    
    C 010 安息の地を求めて
    
    """

    # ***データー入力***
    noize = [int(lp0) for lp0 in input().split()]
    # print("工事x, 工事y, 範囲 " + str(noize))
    for lp1 in range(int(input())):
        wood = [int(lp2) for lp2 in input().split()]
        # print("木陰x, 木陰y " + str(wood))

        # ***判定***
        print("silent" if ((wood[0] - noize[0]) ** 2) +
                          ((wood[1] - noize[1]) ** 2) >= noize[2] ** 2
              else "noisy")

    """
    
    C 008 文字列の抽出
    
    """

    # ***データー入力***
    cut_word = input().split()
    # print("切り抜き文字は" + str(cut_word))
    inp_word = input()
    # print("入力された文字列は " + str(inp_word))

    # ***文字列の整理***
    ans_list = []
    while inp_word.count(cut_word[0]) > 0 and inp_word.count(cut_word[1]) > 0:
        front_num = (inp_word.find(cut_word[0])) + len(cut_word[0])  # 1文字目が見つかった場所に1文字目の文字数を足す
        # print("前半カットする文字数は " + str(front_num))
        inp_word = inp_word[front_num:]
        # print("前半カット後の文字列は " + str(inp_word))
        rear_num = inp_word.find(cut_word[1])
        # print("後半カットの文字の場所は " + str(rear_num))
        ans_list.append(inp_word[:rear_num])
        # print("答えのリスト" + str(ans_list))
        inp_word = inp_word[rear_num + len(cut_word[1]):]  # 後半のカット文字が見つかった場所に文字列を足してスリット
        # print("後半カット後の文字列は " + str(inp_word))

    # ***表示***
    for ans_word in ans_list:
        print("<blank>" if len(ans_word) == 0 else ans_word)

    """
    
    C 006 ハイスコアランキング
    
    """

    import numpy as np

    # ***基本データー入力***
    point_list = []
    inp_num = [int(lp0) for lp0 in input().split()]
    # print("データーの数, 人数, 表示:" + str(inp_num))
    point_mag = [float(lp1) for lp1 in input().split()]
    # print("ポイント倍率" + str(point_mag))
    np_mag = np.array(point_mag)

    # ***各アイテム数の入力***
    for lp2 in range(inp_num[1]):
        item_date = [int(lp3) for lp3 in input().split()]
        # print("各人のアイテムデータ" + str(item_date))

        # ***計算***
        np_list = np.array(item_date)
        cal_point_list = np_mag * np_list
        # print("計算後のポイント" + str(cal_point_list))
        total_point = sum(cal_point_list)
        # print("総ポイント" + str(total_point))
        point_list.append(int(total_point + 0.5))  # roundを使うと不正解が出るので0.5足して切り捨てる
    sort_list = sorted(point_list, reverse=True)
    # print("ポイント上位からのリスト" + str(sort_list))

    # ***表示***
    for lp4 in range(inp_num[2]):
        print(int(sort_list[lp4]))

    """
    
    C 005 アドレスの調査
    
    """

    import numpy as np

    # ***データー入力***
    for lp0 in range(int(input())):

        # ***判定***
        try:
            inp_num = [int(lp1) for lp1 in input().split(".")]
            # print("入力された数字は" + str(inp_num))
            if len(inp_num) == 4:
                np_list = np.array(inp_num)
                print("True" if (0 <= np_list).all() & (np_list <= 255).all() else "False")
            else:
                print("False")
        except:
            print("False")

    """
    
    D073 文字の反転
    
    """

    inp_word = input()
    ans_list = list(inp_word)
    ans_list.reverse()
    # print(ans_list)

    for lp0 in ans_list:
        print(lp0, end="")

    """
    
    D072 データーのバックアップ
    
    """

    inp_num = [int(lp0) for lp0 in input().split()]
    # print(inp_num)

    amari = inp_num[0] % inp_num[1]
    ans = int(inp_num[0] / inp_num[1])
    if amari > 0:
        print(inp_num[2] * (ans + 1))
    else:
        print(inp_num[2] * ans)

    """
    
    D 071 洗濯物と砂埃
    
    """
    num = [int(lp0) for lp0 in input().split()]
    # print(num)
    if num[0] >= 25 or num[1] <= 40:
        print("No" if num[0] >= 25 and num[1] <= 40 else "Yes")
    else:
        print("No")

    """
    
    D070 ほんの残りページ
    
    """

    num = [int(lp0) for lp0 in input().split()]
    print(num[0] - num[1])

    """
    
    D 069 割り切れない平均点
    
    """

    num = [int(lp0) for lp0 in input().split()]
    print("{:.1f}".format(sum(num) / len(num)))

    """
    
    D 068 雨と晴れの日の記録
    
    """

    day = int(input())
    sun = input()
    ans = int(sun.count("S"))
    print("{} {}".format(ans, (day - ans)))

    """
    
    D 067 スイッチのON、OFF
    
    """
    num = int(input())
    print("OFF" if num % 2 == 0 else "ON")
    """
    
    D066 スタミナの計算
    
    """

    num = [int(lp0) for lp0 in input() .split(" ")]
    print((num[1] - num[0]) if num[0] <= num[1] else "No")

    """
    
    D 065 エラーコードの分類
    
    """

    num = input()
    print(num[:1])
    if num[:1] == "2":
        print("ok")
    elif num[:1] == "4":
        print("error")
    else:
        print("unknown")

    """
    
    D064 うそつきの日
    
    """

    word = input()
    if "False" in word:
        print(word.replace("False", "True"))
    else:
        print(word)

    """
    
    D 063 お花見の場所取り
    
    """
    count = 1
    num = [int(lp0) for lp0 in input().split(" ")]
    my = int(input())
    for lp1 in num:
        if my < lp1:
            break
        else:
            count += 1
    print(count)

    """
    
    D 062 ひな祭り
    
    """

    word = "ABCDEFGHIJ"
    num = [int(lp0) for lp0 in input().split(" ")]
    print(word[0:num[0]])
    print(word[num[0]:num[0] + num[1]])
    print(word[num[0] + num[1]:num[0] + num[1] + num[2]])

    """
    
    D 061 3倍返し
    
    """

    num = int(input())
    print("1" if num == 0 else (num * 3))

    """
    
    0D 059 トランプ占い
    
    """
    card = input().split(" ")
    print("{} {}".format(card[0],"Q")
          if "J" is card[0] is card[1] else
          "{} {}".format(card[0], card[1]))
    """
    
    D 058 初詣
    
    """
    num =[int(lp0) for lp0 in input().split(" ")]
    print(("A" * num[0]) + ("B" * num[1]) + ("A" * num[2]))
    """
    
    D 057 プレゼント選び
    
    """

    men = int(input())
    pre = [lp0 for lp0 in input().split(" ")]
    print(pre[men - 1])

    """
    
    D 056 かまくらつくり
    
    """

    hen = [int(lp0) for lp0 in input().split(" ")]
    print((hen[0] ** 3) - (hen[1] ** 3))

    """
    
    D 055 ワインのキャッチコピー
    
    """

    wine = input().split(" ")
    print("Best in {} {}".format(wine[0], wine[1]))

    """
    
    D 054 11/11
    
    """

    word = input()
    # print(len(word))
    print("OK" if len(word) >= 11 else (11 - int(len(word))))

    """
    
    D 053 トリック オア トリート
    
    """

    word = input()
    print("Thanks!" if (word == "candy") or (word == "chocolate")
          else "No!")

    """
    
    D 052 ピラミッドの作り方
    
    """
    num = 0
    for lp0 in range(int(input())):
        num += (lp0 + 1)
    print(num)

    """
    
    D051 衣替え
    
    """

    huku = [lp0 for lp0 in input().split(" ")]
    # print(huku)
    print("OK" if huku.count("W") >= 5 else "NG")

    """
    
    D 050 お月見だんご
    
    """

    num = [int(lp0) for lp0 in input().split(" ")]
    # print(num[0],  num[1])
    if num[0] > 5:
        num[0] = 5
    if num[1] > 5:
        num[1] = 5
    print(num[0] + num[1])

    """
    
    D 049 食欲の秋
    
    """
    word = input()
    if word[-5] == "noaki":
        print(word[-5])
    print(word)

    """
    
    D 048 台風の間隔
    
    """

    taihu = [int(input()) for lp0 in range(5)]
    print(taihu[1] - taihu[0])
    print(taihu[2] - taihu[1])
    print(taihu[3] - taihu[2])
    print(taihu[4] - taihu[3])

    """
    
    D 046 不思議な卵
    
    """

    egg = [int(lp0) for lp0 in input().split()]
    print(max(egg))

    """
    
    D 047 メダリストの表示
    
    """

    world = [input() for lp0 in range(3)]
    print("Gold {}".format(world[0]))
    print("Silver {}".format(world[1]))
    print(("Bronze {}".format(world[2])))

    """
    
    D 045 通知表
    
    """

    word = input()
    print("A" if word == "5" else "B" if word == "4" else "C"
    if word == "3" else "D" if word == "2" else "E")

    # あっこさんの
    print(chr((5 - int(input())) + ord('A')))

    """
    
    D 044 はじめまして
    
    """

    men = input().split()
    print("Hi, Mr. {}".format(men[0]) if men [1] == "M" else "Hi, Ms. {}".format(men[0]))

    """
    
    D 043 天気の表示
    
    """

    rain = int(input())
    print("sunny" if rain <= 30 else "cloudy" if 31 <= rain <= 70 else "rainy")

    """
    
    D 042 行列
    
    """

    num1 = [int(lp0) for lp0 in input().split(" ")]
    num2 = [int(lp1) for lp1 in input().split(" ")]
    print((num1[0] * num2[1]) - (num2[0] * num1[1]))

    """
    
    D 041 本棚選び
    
    """

    book = [int(lp0) for lp0 in input().split(" ")]
    tana = book[1] * book[2]
    print("OK" if book[0] <= tana else "NG")

    """
    
    D 040 連休の天気
    
    """

    ans = 0
    for lp0 in range(7):
        ame = int(input())
        if ame <= 30:
            ans += 1
    print(ans)

    """
    
    D 039 正三角形かどうか
    
    """

    long = [int(input()) for lp0 in range(3)]
    print("YES" if long[0] == long[1] == long[2] else "NO")

    # スマート
    long = [int(input()) for lp0 in range(3)]
    print("YES" if long[0] is long[1] is long[2] else "NO")
    """
    
    D 038 試合の回数
    
    """

    men = int(input())
    print(int(men * (men - 1) / 2))

    """
    
    D 037 花粉症でつらい
    
    """

    box = int(input())
    after = int(input())
    ans = int(after / box)
    amari = after % box
    print(ans if amari == 0 else (ans + 1))

    # あっこさんの
    inpm = int(input())
    inpn = int(input())
    print(int((inpn + (inpm * 0.999)) // inpm))

    """
    
    D 036 アットマーク
    
    """

    word = input()
    print(word.replace("at", "@"))

    """
    
    D 035 日付のデータ
    
    """

    day = input().split(" ")
    print("{}/{}/{}".format(day[0], day[1], day[2]))

    """
    
    D034 どれにしようかな
    
    """
    # 修正後
    num = int(input())
    print((21 % num) if (21 % num) != 0 else num)

    # 修正前
    num = int(input())
    ans = 21 % num
    print(num if ans == 0 else ans)

    """
    
    D 033 頭文字
    
    """

    name = input().split(" ")
    print("{}.{}".format(name[0][:1], name[1][:1]))

    """
    
    D 032 充電時間
    
    """
    # 修正後
    print(100 - int(input()))

    # 修正前
    num = int(input())
    print(100 - num)

    """
    
    D 031 分から秒へ
    
    """
    # 修正後
    print(60 * int(input()))

    # 修正前
    num = int(input())
    print(num * 60)

    """
    
    D 029 さいころの裏面
    
    """
    # 修正後
    print(7 - int(input()))

    # 修正前
    num = int(input())
    print(7 - num)

    """
    
    D 028 数字の桁数
    
    """
    # 修正後
    print(len(input()))

    # 修正前
    ans = [num for num in input()]
    print(len(ans))

    # あっこさんの
    print(len(str(int(input()))))

    """
    
    D 027 nまでの和
    
    """
    # 修正後
    print(sum(range(0, int(input()) + 1)))

    # 修正前
    ans = 0
    num = int(input())
    for i in range(0, num + 1):
        ans += i
    print(ans)

    """
    
    D 026 一週間の予定
    
    """

    week = []
    for day in range(7):
        holyday = input()
        week.append(holyday)

    print(week.count("no"))

    # あっこさんの
    week = [input() for lp0 in range(7)]
    print(week.count("no"))

    """
    
    D 025 数字の出力
    
    """

    num = input()
    if len(num) == 1:
        print("00" + num)
    elif len(num) == 2:
        print("0" + num)
    else:
        print(num)

    # あっこさんの
        inp = int(input())
        print("{:03d}".format(inp))

    """
    
    D 024 三角形の総和
    
    """

    num1 = int(input())
    num2 = int(input())
    print(180 - num1 - num2)

    # エラーを考慮するなら
    while True:

        try:
            num1 = int(input())
            num2 = int(input())
            break
        except:
            print("半角数字を入力してください")

    ans = (180 - num1 - num2)
    print((180 - num1 - num2) if ans >= 0 else "三角形の内書くの条件外です")

    """
    
    D022 表面積の計算
    
    """

    num = int(input())
    print((num ** 2) * 6)

    """
    
    D023 Aの個数
    
    """

    word = input()
    print(word.count("A"))

    """

    
    D021 文字列の一致
    
    """

    word1 = input()
    word2 = input()
    print("Yes" if word1 == word2 else "No")

    """
    
    D019 文字列からN番目
    
    """

    list = input().split()
    num = (int(list[-1]) - 1)
    print(list[0][num])

    """
    
    D 017 最大と最小
    
    """

    num = [int(input()) for lp0 in range(5)]
    print(max(num))
    print(min(num))

    """
    
    D 016 N文字までの出力
    
    """

    word = input()
    print(word[:int(input())])

    """
    
    D015 カウントダウン
    
    """
    num = int(input())
    for lp1 in range(num, 0, -1):
        print(lp1)

    """
    
    D014 小文字を大文字に
    
    """

    word = input()
    print(word.upper())

    """
    
    D013 割り算
    
    """

    list = [int(lp0) for lp0 in input().split()]
    print("{} {}".format(int(list[0] / list[1]), list[0] % list[1]))

    """
    
    D012 絶対値を求めよ
    
    """

    num = int(input())
    print(abs(num))

    # 一行
    print(abs(int(input())))

    """
    
    D011 アルファベットで何番目
    
    """

    english = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
               "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    word = input()
    print(english.index(word) + 1)

    # あっこさんの
    word = input()
    print(ord(word) - ord("A") + 1)

    """
    
    D 010 Eメールアドレス
    
    """

    word = [input() for lp0 in range(2)]
    print("{}@{}".format(word[0], word[1]))

    """
    
    D 009 西暦の計算
    
    """

    num = [int(lp0) for lp0 in input().split()]
    print(num[1] - num[0])

    """
    
    D 008 基数か偶数か
    
    """

    num = int(input())
    print("even" if num % 2 == 0 else "odd")

    """
    
    D 007 N倍の文字列
    
    """

    num = int(input())
    print("*" * num)

    """
    
    D006 単位の計算
    
    """

    inp = [lp0 for lp0 in input().split()]
    num = (int(inp[0]) * 10)
    print(num if inp[1] == "cm" else (num * 100) if inp[1] == "m" else (num * 100000))

    """
    
    D005 等差数列
    
    """
    # 修正後

    num = [int(lp0) for lp0 in input().split()]
    ans = [str(lp1) for lp1 in range(num[0], (num[0] + num[1] * 10), num[1])]
    print(" ".join(ans))

    # 修正前

    n, m = [int(i) for i in input().split()]
    list = []
    for num in range(n, m + (n * 10), m):
        list.append(num)
    list2 = map(str, list)
    print(" ".join(list2))

    """
    
    D 004 文字列の結合
    
    """

    word = [input() for lp0 in range(int(input()))]
    print("Hello " + ",".join(word) + ".")

    """
    
    D 003 掛け算のリスト
    
    """
    num = int(input())
    ans = [str(lp0 * num) for lp0 in range(1, 10)]
    print(" ".join(ans))

    """
    
    D002 数の比較
    
    """

    # 7/3 再更新
    num = [int(lp0) for lp0 in input().split()]
    print("eq" if num[0] == num[1] else max(num))

    # 旧
    num1, num2 = [int(lp0) for lp0 in input().split()]
    if num1 > num2:
        print(num1)
    elif num2 > num1:
        print(num2)
    else:
        print("eq")

    # 内包表記
    num1, num2 = [int(lp0) for lp0 in input().split()]
    print(num1 if num1 > num2 else num2 if num2 > num1 else "eq")

    """
    
    paiza暗号化複合化
        
    """

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

    """

    桂乃梨子

    """

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

    """
    
    その２

    """

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

"""

イベント サラリーマン巡回問題

"""

import math

# データー入力
grid_list = []
long_list = []
for lp0 in range(int(input())):
    inp_num = [int(lp1) for lp1 in input().split()]
    # print("座標 inp_num: " + str(inp_num))
    grid_list.append(inp_num)
    long_num = (inp_num[0] ** 2) + (inp_num[1] ** 2)
    sq_num = math.sqrt(long_num)
    long_list.append(sq_num)

# 最短の処理
ans_list = []
while len(grid_list) > 0:
    # print("処理する座標: " + str(grid_list))
    # print("原点からの距離: " + str(long_list))
    min_num = min(long_list)
    ind_num = long_list.index(min_num)
    ans_list.append(grid_list.pop(ind_num))
    del long_list[ind_num]
    # print("最短コース: " + str(ans_list))
    # print("最短座標を除いた残りの座標リスト: " + str(grid_list))

# 表示
for lp2 in ans_list:
    print(lp2[0], lp2[1])