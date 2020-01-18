#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2020/01/18 09:45'

import wiringpi as pi
import time

"""
初期設定
"""
pi.wiringPiSetupGpio()
i2c = pi.I2C()
ht16k33_adr = i2c.setup(0x70) # スレーブアドレス
i2c.writeReg8(ht16k33_adr, 0x21, 0x01) # レジスタ0x21の設定
i2c.writeReg8(ht16k33_adr, 0x81, 0x01) # レジスタ0x81の設定

"""
変数指定
"""
print_char = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7c, 0x07, 0x7f, 0x67, 0x40]

"""
本体
"""

def main():
    count = 0
    print_n = [0, 0, 0, 0]
    err_mes = "0~9の数字を入れてください。"

    # 初期の 0000 を表示
    for i in range(4):
        i2c.writeReg8(ht16k33_adr, i * 2, print_char[print_n[i]])

    # 4桁の数字を入力 0~9までの数字以外は入力しなおし
    while count < 4:
        try:
            n = int(input(err_mes + "{}桁目".format(count + 1)))
            if n < 0 or n >  10:
                print(err_mes)
                continue

        except ValueError:
            print(err_mes)
            continue

        print_n[count] = n
        count += 1

    print_n.reverse()

    # 表示
    for i in range(4):
        i2c.writeReg8(ht16k33_adr, i * 2, print_char[print_n[i]])

if __name__ == '__main__':
    main()