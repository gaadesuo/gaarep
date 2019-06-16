import os

file_name = ["hogehoge.txt", "piyopiyo.exe"]

for name in file_name:
    path = os.path.join("C:\Python34", name)
    print(path)