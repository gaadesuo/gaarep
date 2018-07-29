# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/07/29 18:28'


def main():

    # ファイルからユーザーIDとパスワードを辞書へ登録
    user_dick = {}
    with open("0_0_pass.txt") as password_file:
        for txt in password_file:
            user_id, user_pass = txt.split(":")
            strip_pass = user_pass.strip()
            user_dick[user_id] = strip_pass
        # print(user_dick)
        password_file.close()

    # 辞書のkeyからユーザーIDをチェック。登録済みならパスワードのチェック
    print("ユーザー名を入力してください。")
    inp_id = input(">>> ")
    if inp_id in user_dick:
        miss = 0
        while miss < 3:
            print("パスワードを入力してください。")
            inp_password = input(">>> ")
            if user_dick[inp_id] == inp_password:
                print("認証されました。")
                break
            else:
                miss += 1
        else:
            print("アクセスが拒否されました。終了します。")

    # 新規IDの場合IDとパスワードをファイルへ書き込み
    else:
        print("ユーザーIDが見つかりません。")
        print("新規登録をする場合は【y】を入力してください")
        inp_word = input(">>> ")
        if inp_word == "y":
            print("ok")
        else:
            print("もう一度やり直してください")


if __name__ == '__main__':
    main()