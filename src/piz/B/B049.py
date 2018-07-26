# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2017 / 12 / 28

txt_list = []
try:
    with open("B49", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
    inp_txt.close()
    # print("入力されたテキストデータのリストは: {}".format(txt_list))

except FileNotFoundError:
    pass

word_list = []
if len(txt_list) == 0:
    inp_num = list(map(int, input().split()))
    for lp0 in range(inp_num[1]):
        word_list.append(input())
else:
    # 後でもう一度入力が行われるので使った要素は消す
    inp_num = list(map(int, txt_list[0].split()))
    del txt_list[0]
    for index in range(inp_num[1]):
        word_list.append(txt_list[index])
    for lp0 in range(inp_num[1]):
        del txt_list[0]
    # print("使い終わった後のリストは: {}".format(txt_list))


# print("人数: {}, 文字リスト: {}, 発言回数: {}".format(inp_num[0], inp_num[1], inp_num[2]))
# print("しりとりの単語リストは: {}".format(word_list))

# 参加人数のリスト作成
men_list = []
for men in range(inp_num[0]):
    men_list.append(men)
print("参加者のリストは: {}".format(men_list))
# 削除されたときの人インデックスがずれるため削除した人間の数をカウント
del_num = 0

before_word = ""
for lp1 in range(inp_num[2]):
    # 一人しかいない場合はそのまま結果発表へ
    if len(men_list) == 1:
        break
    # 今誰が発言してるかを決める。削除された人がいるならその分前にずれる
    men_index = lp1
    while men_index >= len(men_list):
        men_index -= len(men_list)
    men_index -= del_num
    men_no = men_list[men_index]
    print("現在の発言者は: {}".format(men_no))
    if len(txt_list) == 0:
        speech = input()
    else:
        speech = txt_list[0]
        del txt_list[0]
    print("しりとりの発言は{}".format(speech))
    # 発言がリストにあるか確認
    if speech in word_list:
        # 発言の最後がzかの確認
        if speech[-1] == "z":
            print("最後の文字がzの為{}が脱落".format(men_no))
            del men_list[men_index]
            print("残りの人数のリスト: {}".format(men_list))
            del_num += 1
            before_word = ""
        else:
            # 最初の一回目は前回の文字がないので無条件
            if before_word == "":
                pass
            else:
                # 前回の文字の剤事今回の最初があってるかの確認
                if before_word[-1] == speech[0:1]:
                    # print("前回と一緒の為成功")
                    pass
                else:
                    print("前回の文字の最後が合わないため{}が脱落".format(men_no))
                    del men_list[men_index]
                    print("残った人数のリスト: {}".format(men_list))
                    del_num += 1
                    before_word = ""
            before_word = speech
            word_list.remove(speech)
            print("合格なので単語リストから【{}】を削除。残ったリストは: {}".format(speech, word_list))

    else:
        print("リストにない文字を使ったので{}が脱落".format(men_no))
        del men_list[men_index]
        print("残った人数のリスト: {}".format(men_list))
        del_num += 1
        before_word = ""

print(len(men_list))
for ans in men_list:
    print(ans + 1)