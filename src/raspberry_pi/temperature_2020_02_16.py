#! python3
# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2020/02/16 09:05'

# I2C用ライブラリ
import smbus

def main():
    """
    初期設定
    """
    # コネクションオブジェクトの取得
    bus = smbus.SMBus(1)
    adt7410_addr = 0x48
    adt7410_reg = 0x00
    # 下のconfは読み出しbitの設定場所
    adt7410_conf = 0x03



    """
    読み出し
    """

    therm_date = []

    # メソッド configration_adt7410, 0x00 で13bit読み出し
    # 16bitで読み出すなら 0x00を0x80へ変更。

    # 13bit
    bus.write_word_date(adt7410_addr, adt7410_conf, 0x00)
    therm_date.append(bus.read_word_date(adt7410_addr, adt7410_reg))
    # 16bit
    bus.write_word_date(adt7410_addr, adt7410_conf, 0x80)
    therm_date.append(bus.read_word_date(adt7410_addr, adt7410_reg))

    print(therm_date)


if __name__ == '__main__':
    main()