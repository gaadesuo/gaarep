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
    # コネクションオブジェクトの取得。
    bus = smbus.SMBus(1)
    adt7410_addr = 0x48
    adt7410_reg = 0x00
    # 下のconfは読み出しbitの設定場所。
    adt7410_conf = 0x03

    # print(bus)

    """
    読み出し
    """

    # メソッド configration_adt7410, 0x00 で13bit読み出し。
    # 16bitで読み出すなら 0x00を0x80へ変更。

    # 13bit
    bus.write_word_data(adt7410_addr, adt7410_conf, 0x00)
    thermo_date_13 = bus.read_word_data(adt7410_addr, adt7410_reg)
    print("スレーブの値 13bit {}".format(hex(thermo_date_13)))
    # 16bit
    bus.write_word_data(adt7410_addr, adt7410_conf, 0x80)
    thermo_date_16 = bus.read_word_data(adt7410_addr, adt7410_reg)
    print("スレーブの値 16bit {}".format(hex(thermo_date_16)))

    # 上位、下位byteの入れ替え。
    # 上位1byteを8bit右へシフト、下位1byteを8bit左へシフト。
    change_date_13 = (thermo_date_13 & 0xff00) >> 8 | (thermo_date_13 & 0xff) << 8
    change_date_16 = (thermo_date_16 & 0xff00) >> 8 | (thermo_date_13 & 0xff) << 8
    print("上位、下位byteを並べ替えた後 13bit {}".format(hex(change_date_13)))
    print("上位、下位byteを並べ替えた後 16bit {}".format(hex(change_date_16)))
    print("2進数表記 13bit {}".format(bin(change_date_13)))
    print("2進数表記 16bit {}".format(bin(change_date_16)))

    # 13bitを3bit右にシフト
    change_date_13 = change_date_13 >> 3
    print("3bit移動後 13bit {}".format(bin(change_date_13)))

    print("10進数表記 13bit {}".format(change_date_13))
    print("10進数表記 16bit {}".format(change_date_16))

    print("温度 13bit {}".format(change_date_13 / 16))
    print("温度 16bit {}".format(change_date_16 / 128))



if __name__ == '__main__':
    main()