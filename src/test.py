word_dick_list = [
    {"t": list("ty"), "g": list("gh"), "b": list("bn"), "y": list("yt"), "h": list("hg"), "n": list("nb")},
    {"r": ["r", "e", "f", "t"], "f": ["f", "r", "d", "v", "g"], "v": ["v", "f", "c", "b"]}]

flag = 0
ans = 0

inp_word = list(input())

for num in range(len(inp_word)):
    print("押したキーは" + str(inp_word[num]))
    dick = word_dick_list[flag]
    print("今回使う辞書" + str(dick))
    if inp_word[num] in dick:
        # 入力された文字が辞書のキーに登録されていればTrue
        for ng_word in dick:
            # 初めての範囲枠ならフラグを立てる。今回の入力文字を代入
            if flag == 0:
                flag = 1
                befoer_word = dick[inp_word[num]]
                print("範囲枠上なので次回のNGキー'" + str(befoer_word))
                print(flag)
                break

            # 前回範囲枠なので規定文字の場合カウントを増やす
            else:
                print(flag)
                if befoer_word.count(ng_word) > 0:
                    ans += 1
                    befoer_word = dick[ng_word]
                    print("タッチミス発生。次回のカウントきーは'" + str(befoer_word))
                    break
                else:
                    flag = 0
    else:
        flag = 0
print(ans)