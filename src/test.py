# ***データ入力***
vs_1_1 = [int(lp0) for lp0 in input().split()]
vs_1_2 = [int(lp1) for lp1 in input().split()]
vs1_time = [int(lp2) for lp2 in input().split()]
vs2_time = [int(lp3) for lp3 in input().split()]
# print("1回戦1試合目の対戦者" + str(vs_1_1))
# print("1回戦2試合目の対戦者" + str(vs_1_2))
# print("1回戦のタイム" + str(vs1_time))
# print("2回戦のタイム" + str(vs2_time))

# ***処理と表示***
vs2_1 = vs_1_1[0] if vs1_time[vs_1_1[0] - 1] < vs1_time[vs_1_1[1] - 1] else vs_1_1[1]
# print("1回戦1試合目の勝者は" +str(vs2_1))
vs2_2 = vs_1_2[0] if vs1_time[vs_1_2[0] - 1] < vs1_time[vs_1_2[1] - 1] else vs_1_2[1]
# print("1回戦2試合目の勝者は" + str(vs2_2))
vs_2 = [vs2_1, vs2_2]
if vs2_time[0] < vs2_time[1]:
    print(min(vs_2))
    print(max(vs_2))
else:
    print(max(vs_2))
    print(min(vs_2))