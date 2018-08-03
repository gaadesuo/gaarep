# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/07/29 18:28'


def file_read():
    """
    ファイルからユーザーIDとパスワードを辞書へ入れる
    :return: dic
    """

    u_dick = {}
    with open("0_0_pass.txt", "r", encoding="utf-8") as password_file:
        for txt in password_file:
            user_id, user_pass = txt.split(":")
            strip_pass = user_pass.strip()
            u_dick[user_id] = strip_pass
        # print(user_dick)
        password_file.close()
    return u_dick


def input_word(desc, l_num, g_num):
    """
    文字の入力と説明文
    :param desc: 入力の説明文
    :return: 入力された文字
    """
    print("{}【半角英小文字 半角数字で{}文字～{}文字】".format(desc, l_num, g_num))
    return input(">>> ")


def word_check(inp_word, l_num, g_num):
    """
    入力された文字が半角英数か、そして指定の文字数なのかを調べる
    :param inp_word: 入力された文字
    :param l_num: 最低文字数
    :param g_num: 最高文字数
    """
    # 入力文字数の判別
    if len(inp_word) < l_num or len(inp_word) > g_num:
        print("指定の文字数で入力してください。")
        return False
    # スキーコードから半角英数文字化の判別
    for word in list(inp_word):
        if 48 < ord(word) < 57 or 96 < ord(word) < 123:
            pass
        else:
            print("半角英数で入れてください。")
            return False
    return True


def pass_check(u_dick, inp_id):
    """
    パスワードのチェック。3回ミスで終了
    :param u_dick: 登録中のファイルの辞書
    :param inp_id: 入力されたID
    """
    miss = 0
    while miss < 3:
        print("パスワードを入力してください。")
        inp_password = input(">>> ")
        if u_dick[inp_id] == inp_password:
            print("認証されました。")
            break
        else:
            miss += 1
    else:
        print("アクセスが拒否されました。終了します。")


def id_miss():
    """
    ユーザーIDが見つからなかった場合
    :return:True, False
    """
    print("ユーザーIDが見つかりません。")
    print("新規登録をする場合は【y】を入れてエンターを押してください。")
    print("終了する場合は【n】を入れてエンターを押してください。")
    print("もう一度ユーザーIDを入れる場合はそのままエンターを押してください。")
    inp_word = input(">>> ")
    if inp_word == "y":
        return "y"
    elif inp_word == "n":
        print("終了します。")
        return "n"
    else:
        return "c"


def id_write(id_dic):
    """
    新規登録
    IDとパスワードをチェック後問題がなければファイルに保存
    :param id_dic: 登録されたIDとパスワードの辞書
    """
    new_id_pass_list = []
    while len(new_id_pass_list) < 1:
        print("新規登録を開始します。")
        new_id = input_word("登録するユーザーIDを入れてエンターを押してください。", 4, 8)
        if word_check(new_id, 4, 8):
            pass
        else:
            continue
        # 既存IDと登録IDが同じものがあるかのチェックと登録
        if new_id in id_dic:
            print("そのIDは使用中の為別のIDで登録してください。")
            continue
        print("登録するIDは【{}】でよろしいですか？".format(new_id))
        print("よろしければ【y】を、違う場合は【n】を、終了する場合は【e】を入力してエンターを押してください。")
        inp_word = input(">>> ")

        if inp_word == "y":
            new_id_pass_list.append(new_id)

            # パスワードのチェックと登録
            while True:
                print("登録するパスワードを2回入力してください")
                pass_1 = input_word("一回目", 4, 12)
                pass_2 = input_word("二回目", 4, 12)
                if pass_1 == pass_2 and word_check(pass_1, 4, 12):
                    new_id_pass_list.append(pass_1)
                    print("パスワードは【{}】でよろしいですか？".format(new_id_pass_list[1]))
                    print("よろしければ【y】を押してエンターを押して下さい。入力をやり直す場合はそのままエンターを押してください。")
                    inp_word_2 = input(">>> ")
                    if inp_word_2 == "y":
                        with open("0_0_pass.txt", "a", encoding="utf-8") as password_file:
                            write_word = ":".join(new_id_pass_list) + "\n"
                            # print(write_word)
                            password_file.write(write_word)
                            password_file.close()
                        break
                    else:
                        continue
                else:
                    print("パスワードgは間違っているか、規定外のパスワードです。もう一度入力してください。")

        elif inp_word == "e":
            print("新規登録を終了します。")
            break


def main():

    while True:
        inp_id = input_word("登録されているユーザーIDを入れてください。", 4, 8)
        user_dick = file_read()
        # print(user_dick)
        if word_check(inp_id, 4, 8):
            if inp_id in user_dick:
                pass_check(user_dick, inp_id)
                break
            else:
                select_word = id_miss()
                if select_word == "y":
                    id_write(user_dick)
                elif select_word == "c":
                    pass
                else:
                    break


if __name__ == '__main__':
    main()