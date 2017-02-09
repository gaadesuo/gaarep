#-----初期設定-----


payments = []


#-----初期表示-----


print('''収支金額を入力半角数字でしてください。
入力が終わったらzキーを入れてください。''')


#-----数字確認と入力-----


while True:
    inport = input('>>> ')
    if inport == "z":
        break

    # 数字の確認 数字ならtrue、それ以外ならfalesを返す
    ng = inport.isdigit()

    #fales比較は0で比較する。tureなら1
    if ng == 0:
    
        print(u'半角数字を入れてください')
        continue
   
    else:
        #ここで文字列を数値に直す
        num = int(inport)
        payments.append(num)


#----代入と計算-----


fre = len(payments)
max = max(payments)
min = min(payments)
tot = sum(payments)
ave = tot / fre
sml = sorted(payments)


#-----出力-----

print(u'入力された金額をソート表示します。')
for money in payments:
    print(str(money) + u'円')
print(u'''-------------------------------------------------------------------------------------------
入力された収支は''' + str(fre) +  '''回です。
その内、最大収支は''' + str(max) + '''円でした。
また、最小収支は''' + str(min) + '''円でした。
収支の合計金額は''' + str(tot) + '''円です。
平均金額は''' + str(ave) + '円でした。')
