# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/23 :09:44$'

import RPi.GPIO as PIN
import time


def main():
    pass


def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    """
    MCP3208からSPI通信で12bitのデジタル値を取得
    0～7の8チャンネル使用可能
    :param adcnum: int: MCP3208のチャンネル設定 
    :param clockpin: int: SPI CLOCKPINのGPIO番号 MCP3208側はCLK
    :param mosipin:  int: SPI MOSIPINのGPIO番号 MCP3208側はD_IN
    :param misopin: int: SPI MISOPINのGPIO番号 MCP3208側はD_OUT
    :param cspin: int: SPI CEOPINのGPIO番号 MCP3208側はCS/SHDN
    :return: int: 電圧のデジタル値
    """

    if adcnum > 7 or adcnum < 0:
        return -1

    # 初期設定
    PIN.output(cspin, PIN.HIGH)
    PIN.output(clockpin, PIN.LOW)
    # cspinをHIGHにして通信開始
    PIN.output(cspin, PIN.LOW)

    # 通信信号、チャンネル設定、チャンネル番号の設定
    # 設定は上位5bitの為3bitずらして上位５bitにする
    commandout = adcnum
    commandout |= 0b00011000
    commandout <<= 3

    # 設定の値を1bitづつ送信。1のときはHIGH、0の時はLOW
    for lp1 in range(5):
        if commandout & 0b10000000:
            PIN.output(mosipin, PIN.HIGH)
        else:
            PIN.output(mosipin, PIN.LOW)
        commandout <<= 1
        # 1クロック進めて1bit送信
        PIN.output(clockpin, PIN.HIGH)
        PIN.output(clockpin, PIN.LOW)
    adcout = 0

    # 設定を与えて返ってきた値をadcoutに書き込み、1bitづつずらす。
    # 仕様により最初の1bitはnull
    # HIGHの時に1を書き込み、nullbit含めて13桁。null以外12桁で2進数の値にする
    for lp2 in range(13):
        PIN.output(clockpin, PIN.HIGH)
        PIN.output(clockpin, PIN.LOW)
        adcout <<= 1
        if lp2 > 0 and PIN.input(misopin) == PIN.HIGH:
            adcout |= 0b0001

    # cspinをHIGHにして通信終了し値を返す
    PIN.output(cspin, PIN.HIGH)
    return adcout

if __name__ == '__main__':
    main()

    PIN.setmode(PIN.BCM)

    CLK = 11
    MOSI = 10
    MISO = 9
    CS = 8

    PIN.setup(CLK, PIN.OUT)
    PIN.setup(MOSI, PIN.OUT)
    PIN.setup(MISO, PIN.IN)
    PIN.setup(CS, PIN.OUT)

    try:
        while True:
            side_num = readadc(0, CLK, MOSI, MISO, CS)
            length_num = readadc(1, CLK, MOSI, MISO, CS)
            print("{}".format("横", side_num))
            print("{}".format("縦", length_num))
            time.sleep(1)

    except KeyboardInterrupt:
        pass

    PIN.cleanup()
