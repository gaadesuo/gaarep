# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/08/04 17:26'

import re
import pyperclip

phone_regex = re.compile(r"""(
(\d{1,4}|\(\d{1,4}\)) # 市外局番
(-|\s)
(\d{1,4})             # 市内局番
(-|\s)
(\d{3,4})             # 加入者番号
)""", re.VERBOSE)

mail_regex = re.compile(r"""(
[a-zA-Z0-9._%+-]+ # ユーザー名
@
[a-zA-Z0-9.-]+    # ドメイン
(\.[a-zA-Z{2,4}]+)      # ドットなんとか
)""", re.VERBOSE)

text = str(pyperclip.paste())
print(text)

phone_list = phone_regex.findall(text)
mail_list = mail_regex.findall(text)

print(phone_list, mail_list)