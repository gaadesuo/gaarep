#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2020/01/26 09:10'

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
変数
"""

matrix_row = 8 # マトリクスLEDの行数

# リスト内要素、2進数の並びが左から1列目、要素の行が上から一行目のLEDの位置
out = [ 0b00100100,
        0b11111111,
        0b00000000,
        0b01111110,
        0b11111111,
        0b10100101,
        0b11000011,
        0b11111111]

"""
本体
"""

def main():

    for i in range(matrix_row):
        i2c.writeReg8(ht16k33_adr, i * 2, out[i])


if __name__ == '__main__':
    main()