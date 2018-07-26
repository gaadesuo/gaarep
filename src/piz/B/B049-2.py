# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = 2017 / 12 / 29

txt_list = []

try:
    with open("B49", "r", encoding="utf-8") as inp_txt:
        txt_list = [txt.strip() for txt in inp_txt]
        # print("入力されたテキストデータのリストは: {}".format(txt_list))
        inp_txt.close()
except FileNotFoundError:
    pass

word_list = []
say_list = []
if len(txt_list) == 0:
    inp_date = list(map(int, input().split()))
    for lp0 in range(inp_date[1]):
        word_list.append(input())
    for lp1 in range(inp_date[2]):
        say_list.append(input())
else:
    inp_date = list(map(int, txt_list[0].split()))
    del txt_list[0]
    for lp0 in range(inp_date[1]):
        word_list.append(txt_list[0])
        del txt_list[0]
    for lp1 in range(inp_date[2]):
        say_list.append(txt_list[0])
        del txt_list[0]

# print("しりとりの参加人数: {:0d}, 単語数: {:0d}, 回答数: {:0d}".format(inp_date[0], inp_date[1], inp_date[2]))
# print("単語リスト: {}".format(word_list))
# print("回答リスト: {}".format(say_list))

human_list = []
# 参加者リストの作成
for human in range(inp_date[0]):
    human_list.append(human)
num = len(human_list)
# print("参加者リストを作成: {}".format(human_list))

miss_count = 0
before_word = ""
for lp2 in range(inp_date[2]):
    print("現在の参加者リスト: {}".format(human_list))
    print("現在の単語リスト: {}".format(word_list))
    # 最初から一人、最後の一人になった、単語リストがなくなったら即終了
    if len(human_list) == 1 or len(word_list) == 0:
        break
    else:
        men_no = lp2 - miss_count
        print(lp2, men_no)
        while men_no >= len(human_list):
            men_no -= num
        print(lp2, men_no)
        print("現在の発言者は: {:0d} 回答は: {}".format(human_list[men_no], say_list[lp2]))
        last_word = say_list[lp2][-1:]
        print("回答の最後の文字は{}".format(last_word))
        # 発言が単語リストにあるかのチェック
        if say_list[lp2] not in word_list or last_word == "z":
            print("【ミス】{}が脱落".format(human_list[men_no]))
            del human_list[men_no]
            miss_count += 1

        else:
            print("【成功】 単語({})を削除".format(say_list[lp2]))
            word_list.remove(say_list[lp2])

print("最後まで残った人のリストは{}".format(human_list))

