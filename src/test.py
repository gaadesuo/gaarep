
# -*- coding:utf-8 -*-
txt_r = open("sample.txt","r",encoding="utf_8")

i = 0

while True:
    line = txt_r.readline()
    if line == "":
        break
    print("{:4d}:{}".format(i + 1,line.rstrip("\n")))
    i += 1

txt_r.close()
