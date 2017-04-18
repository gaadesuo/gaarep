# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '$2017/04/18 :10:48$'

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
    :return: 
    """

    if adcnum > 7 or adcnum < 0:
        return -1

    # cspinをHIGHにして通信準備
    PIN.output(cspin, PIN.HIGH)
    PIN.output(clockpin, PIN.LOW)
    # cspinをLOWにして通信開始
    PIN.output(cspin, PIN.LOW)

    commandout = adcnum
    # ループ中はLSB(最下位ビット)から8bit目まに送信するようにする
    # commandout = commandout | 0x18 (|はorで commandoutは半固定抵抗からのアナログ値)
    commandout |= 0x18
    # commandout = commandout << 3 (<<は値分のbit左へシフト。ここでは3)
    commandout <<= 3
    # LSBから数えて8bit目から4bit目までに送信。1ループごとに1bitづつずらす
    for lp1 in range(5):
        if commandout & 0x80:
            # D_INへHIGHのデジタル信号送信elseはLOW
            PIN.output(mosipin, PIN.HIGH)
        else:
            PIN.output(mosipin, PIN.LOW)
        commandout <<= 1
        # 1クロックの信号を与えbitの値を通信させる
        PIN.output(clockpin, PIN.HIGH)
        PIN.output(clockpin, PIN.LOW)
    adcout = 0

    # 13bitを読む(nullbit～12bitデータ)1ループごとに1bitずらす
    for lp2 in range(13):
        # 1クロックの信号を与える
        PIN.output(clockpin, PIN.HIGH)
        PIN.output(clockpin, PIN.LOW)
        adcout <<= 1
        if lp2 > 0 and PIN.input(misopin) == PIN.HIGH:
            adcout |= 0x1
    # cspinをHIGHにして通信終了
    PIN.output(cspin, PIN.HIGH)
    return adcout

if __name__ == '__main__':
    main()
    PIN.setmode(PIN.BCM)

    SPICLK = 11
    SPIMOSI = 10
    SPIMISO = 9
    SPICS = 8
    LED = 25

    # SPI通信用の入出力を定義
    PIN.setup(SPICLK, PIN.OUT)
    PIN.setup(SPIMOSI, PIN.OUT)
    PIN.setup(SPIMISO, PIN.IN)
    PIN.setup(SPICS, PIN.OUT)
    # LEDの出力設定
    PIN.setup(LED, PIN.OUT)

    try:
        while True:
            inputVal0 = readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS)
            print(inputVal0)
            if inputVal0 < 700:
                PIN.output(LED, PIN.HIGH)
            else:
                PIN.output(LED, PIN.LOW)
            time.sleep(0.2)

    except KeyboardInterrupt:
        pass

    PIN.cleanup()