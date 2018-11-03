the_board = {"top_L": " ", "top_M": " ", "top_R": " ",
             "mid_L": " ", "mid_M": " ", "mid_R": " ",
             "low_L": " ", "low_M": " ", "low_R": " "}

turn = 0

check_list = ["top_L", "top_M", "top_R",
              "mid_L", "mid_M", "mid_R",
              "low_L", "low_M", "low_R"]


def check():
    """
    入力された文字がリストにあるかチェック
    wordが正しければ碁盤の辞書に入力
    """
    global turn
    global check_list
    global the_board

    while True:
        w = input(">>> ")
        if w in check_list:
            check_list.remove(w)
            # print(check_list)
            if turn == 0:
                the_board[w] = "o"
                turn = 1
            else:
                the_board[w] = "x"
                turn = 0
            # print(the_board)
            break
        else:
            print("今までに入力されていない入力wordを入れてください")


def p_board():
    """
    碁盤を表示する
    """
    print("{}|{}|{}".format(the_board["top_L"], the_board["top_M"], the_board["top_R"]))
    print("-+-+-")
    print("{}|{}|{}".format(the_board["mid_L"], the_board["mid_M"], the_board["mid_R"]))
    print("-+-+-")
    print("{}|{}|{}".format(the_board["low_L"], the_board["low_M"], the_board["low_R"]))


while True:

    p_board()
    print("")
    print("*** 入力word ***")
    print("top_L top_M top_R")
    print("mid_L mid_M mid_R")
    print("low_L low_M low_R")
    print("")

    if turn == 0:
        print("先手です。今までに入力されていない入力wordを入れてください")
        check()
    else:
        print("後手です。今までに入力されていない入力wordを入れてください")
        check()

    if the_board["top_L"] == the_board["top_M"] == the_board["top_R"] == "o"or\
        the_board["mid_L"] == the_board["mid_M"] == the_board["mid_R"] == "o" or\
        the_board["low_L"] == the_board["low_M"] == the_board["low_R"] == "o" or\
        the_board["top_L"] == the_board["mid_L"] == the_board["low_L"] == "o" or\
        the_board["top_M"] == the_board["mid_M"] == the_board["low_M"] == "o" or\
        the_board["top_R"] == the_board["mid_R"] == the_board["low_R"] == "o" or\
        the_board["top_L"] == the_board["mid_M"] == the_board["low_R"] == "o" or\
            the_board["top_R"] == the_board["mid_M"] == the_board["low_L"] == "o":
        p_board()
        print("先手の勝ちです")
        break

    elif the_board["top_L"] == the_board["top_M"] == the_board["top_R"] == "x" or\
        the_board["mid_L"] == the_board["mid_M"] == the_board["mid_R"] == "x" or\
        the_board["low_L"] == the_board["low_M"] == the_board["low_R"] == "x" or\
        the_board["top_L"] == the_board["mid_L"] == the_board["low_L"] == "x" or\
        the_board["top_M"] == the_board["mid_M"] == the_board["low_M"] == "x" or\
        the_board["top_R"] == the_board["mid_R"] == the_board["low_R"] == "x" or\
        the_board["top_L"] == the_board["mid_M"] == the_board["low_R"] == "x" or\
            the_board["top_R"] == the_board["mid_M"] == the_board["low_L"] == "x":
        p_board()
        print("後手の勝ちです")
        break
