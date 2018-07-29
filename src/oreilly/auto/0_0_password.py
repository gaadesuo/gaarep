# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/07/29 18:28'


def main():
    with open("0_0_pass.txt") as password_file:
        secret_password = password_file.read()
        # print(secret_password)
        password_file.close()

    print("パスワードを入力してください。")
    typed_password = input(">>> ")
    print("認証されました" if typed_password == secret_password
          else "パスワードは脆弱です" if typed_password == "12345"
               else "アクセスが拒否されました。")


if __name__ == '__main__':
    main()