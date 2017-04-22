# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/22 :09:45$'

import RPi.GPIO as PIN
import time
import math


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

    # 通信信号、シングルチャンネル、チャンネル番号の設定設定は頭から5bitのため3bitずらす
    commandout = adcnum
    commandout |= 0b00011000
    commandout <<= 3

    # 設定の値を上位5bitを上位から1bitずつ送信。1のときはhigh、0のときはLOW
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

    # 設定を与えて帰ってきた値をadcoutに書き込み1bitづつずらす。最初の1bitはnull設定
    # HIGHのときは1を書き込みnull含め2進数13桁表示で値を与える
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
            val_num = readadc(0, CLK, MOSI, MISO, CS)
            inp_val = val_num * 0.0008056640625
            print("{:.3f}".format(inp_val))
            X = ((3.3 - inp_val) / inp_val) * 10000
            Y = math.log(float(X) / float(10000) / float(3435))
            Z = 1 / (float(25) + 273.0)
            Temp = (1 / (Y + Z)) - 273

            print(Temp)
            time.sleep(1)

    except KeyboardInterrupt:
        pass

    PIN.cleanup()