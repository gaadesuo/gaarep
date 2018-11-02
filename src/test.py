the_board = {"top_L": " ", "top_M": " ", "top_R": " ",
             "mid_L": " ", "mid_M": " ", "mid_R": " ",
             "low_L": " ", "low_M": " ", "low_R": " "}

print("{}|{}|{}".format(the_board["top_L"], the_board["top_M"], the_board["top_R"]))
print("-+-+-")
print("{}|{}|{}".format(the_board["mid_L"], the_board["mid_M"], the_board["mid_R"]))
print("-+-+-")
print("{}|{}|{}".format(the_board["low_L"], the_board["low_R"], the_board["low_R"]))

if the_board["top_L"] == the_board["top_M"] == the_board["top_R"] == "o"or\
    the_board["mid_L"] == the_board["mid_M"] == the_board["mid_R"] == "o" or\
    the_board["low_L"] == the_board["low_M"] == the_board["low_R"] == "o" or\
    the_board["top_L"] == the_board["mid_L"] == the_board["low_L"] == "o" or\
    the_board["top_M"] == the_board["mid_M"] == the_board["low_M"] == "o" or\
    the_board["top_R"] == the_board["mid_R"] == the_board["low_R"] == "o" or\
    the_board["top_L"] == the_board["mid_M"] == the_board["low_R"] == "o" or\
        the_board["top_R"] == the_board["mid_M"] == the_board["low_L"] == "o":
    print()

elif the_board["top_L"] == the_board["top_M"] == the_board["top_R"] == "x" or\
    the_board["mid_L"] == the_board["mid_M"] == the_board["mid_R"] == "x" or\
    the_board["low_L"] == the_board["low_M"] == the_board["low_R"] == "x" or\
    the_board["top_L"] == the_board["mid_L"] == the_board["low_L"] == "x" or\
    the_board["top_M"] == the_board["mid_M"] == the_board["low_M"] == "x" or\
    the_board["top_R"] == the_board["mid_R"] == the_board["low_R"] == "x" or\
    the_board["top_L"] == the_board["mid_M"] == the_board["low_R"] == "x" or\
        the_board["top_R"] == the_board["mid_M"] == the_board["low_L"] == "x":
    print()