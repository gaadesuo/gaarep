inp_num = list(map(int, input().split()))
# print("人数: {}, 文字リスト: {}, 発言回数: {}".format(inp_num[0], inp_num[1], inp_num[2]))
word_list = []
for lp0 in range(inp_num[1]):
    word_list.append(input())
# print("しりとりの単語リストは: {}".format(word_list))

# 参加人数のリスト作成
men_list = []
for men in range(inp_num[0]):
    men_list.append(men)
# print("参加者のリストは: {}".format(men_list))

befor_word = ""
for lp1 in range(inp_num[2]):
    # 今誰が発言してるかを決める
    men_index = lp1
    while men_index >= len(men_list) or len(men_list) == 1:
        men_index -= len(men_list)
    men_no = men_list[men_index]
    # print("現在の発言者は: {}".format(men_no))
    speech = input()
    # print("しりとりの発言は{}".format(speech))
    # 発言がリストにあるか確認
    if speech in word_list:
        # 発言の最後がzかの確認
        if speech[-1] == "z":
            # print("最後の文字がzの為{}が脱落".format(men_no))
            del men_list[men_index]
            # print("残りの人数のリスト: {}".format(men_list))
            befor_word = ""
        else:
            # 最初の一回目は前回の文字がないので無条件
            if befor_word == "":
                pass
            else:
                # 前回の文字の剤事今回の最初があってるかの確認
                if befor_word[-1] == speech[0:1]:
                    # print("前回と一緒の為成功")
                    pass
                else:
                    # print("前回の文字の最後が合わないため{}が脱落".format(men_no))
                    del men_list[men_index]
                    # print("残った人数のリスト: {}".format(men_list))
            befor_word = speech
            word_list.remove(speech)

    else:
        # print("リストにない文字を使ったので{}が脱落".format(men_no)
        del men_list[men_index]
        # print("残った人数のリスト: {}".format(men_list))
    if len(men_list) == 1:
        break


print(len(men_list))
for ans in men_list:
    print(ans + 1)