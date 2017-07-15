# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/05/07 :20:46$'


def main():
    pass


if __name__ == '__main__':
    main()

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
    
    C 010 安息の地を求めて
    
    """

    # 騒音の広さの情報の取得
    sound = [int(lp) for lp in input().split()]
    # print(sound)

    # 木陰の場所の数
    s_round = int(input())

    # 木陰の情報の取得と計算
    for lp0 in range(s_round):
        wd_list = [int(lp1) for lp1 in input().split()]
        # print(wd_list)
        num1 = ((wd_list[0] - sound[0]) ** 2)
        num2 = ((wd_list[1] - sound[1]) ** 2)
        num3 = int(sound[2]) ** 2
        # print(num1, num2, num3)
        print("silent" if num1 + num2 >= num3 else "noisy")

    """
    
    C 008 文字列の抽出
    
    """

    # tagを入力
    tag = input().split()
    # print(tag)

    # 文字列を入力
    word = input()
    # print(word)

    # 処理
    start = 0
    while True:
        if tag[0] in word[start:] and tag[1] in word[start:]:
            # tag[0]含む文字数を検索
            # print(int(word[start:].find(tag[0])))
            # print(len(tag[0]))
            f_count = int(word[start:].find(tag[0])) + (len(tag[0]))
            # tag[1]が始まるまでの文字数を検索
            r_count = int(word[start:].find(tag[1]))
            # print(f_count + start, r_count + start)
            print(word[f_count + start:r_count + start] if f_count != r_count else "<blank>")
            start = start + r_count + int(len(tag[1]))
            # print(start)
        else:
            break

    # あっこの

        inp1 = input().split()
        inp2 = input()
        inp3 = list()
        inp1l0 = len(inp1[0])
        inp1l1 = len(inp1[1])

        # print(inp1, inp2)

        while len(inp2) > 0:
            spos = inp2.find(inp1[0])
            if spos == -1:
                break;

        epos = inp2.find(inp1[1])
        if epos == -1:
            break;

    rslt = inp2[spos + inp1l0:epos]
    if len(rslt) == 0:
        print('<blank>')
    else:
        print(rslt)
    inp2 = inp2[epos + inp1l1:]

    """
    
    C 006 ハイスコアランキング
    
    """

    # 修正版

    import numpy

    # [0]:種類 [1]:人数 [2]:表示数
    inp_1 = [int(lp0) for lp0 in input().split()]

    # inp[0]個分のパラメーター入力
    inp_2 = [float(lp1) for lp1 in input().split(" ")]
    inp_2_ex = numpy.array(inp_2)
    # print(inp_2_ex)

    # 計算
    date_list = []
    for lp0 in range(inp_1[1]):
        men_date = [int(lp2) for lp2 in input().split()]
        men_date_ex = numpy.array(men_date)
        ans = sum(inp_2_ex * men_date_ex)
        date_list.append(int(ans + 0.5))
    date_list.sort(reverse=True)
    # print(date_list)

    for lp3 in range(inp_1[2]):
        print(date_list[lp3])

    # 80点
    # [0]:種類 [1]:人数 [2]:表示数
    inp_1 = [int(lp0) for lp0 in input().split()]

    # inp[0]個分のパラメーター入力
    inp_2 = [float(lp1) for lp1 in input().split(" ")]

    # inp_1[1]人分のデーターを収納
    date_list = []
    for lp0 in range(inp_1[1]):
        men_date = [int(lp2) for lp2 in input().split()]
        date_list.append(men_date)
    # print(inp_2)
    # print(date_list)

    # ポイントの処理
    ans = []
    ans_list = []
    for lp3 in range(inp_1[1]):
        for lp4 in range(inp_1[0]):
            ans.append(inp_2[lp4] * date_list[lp3][lp4])
        ans_list.append(ans)
        ans = []
    # print(ans_list)

    # 合計ポイントの計算とソート
    all = [int(round(sum(ans_list[lp5]), 0)) for lp5 in range(len(ans_list))]
    all.sort(reverse=True)
    # print(all)

    # 表示
    for lp6 in range(inp_1[2]):
        print(all[lp6])

    """
    
    C 005 アドレスの調査
    
    """

    ip_num = []
    count = int(input())
    for lp0 in range(count):
        try:
            ip = [int(lp1) for lp1 in input().split(".")]
            for lp2 in ip:
                # print(lp2)
                if (lp2 >= 0) & (lp2 <= 255):
                    ip_num.append(lp2)
            # print(ip_num)
            print("True" if len(ip_num) == 4 else "False")
            ip_num = []
        except:
            print("False")

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


amari = []
hako = []
n = 0

# 入力は　機械の数 お菓子の数
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

