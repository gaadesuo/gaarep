# データ入力
win_list = []
lose_list = []
count = (int(input()))
for lp2 in range(count):
    lose_list.append([])
print(lose_list)
loop = int((count ** 2 - count) / 2)
print(loop)
for lp0 in range(loop):
    inp_num = [int(lp1) for lp1 in input().split()]
    print(inp_num)
    lose_list[inp_num[0] - 1].append(inp_num[1])
print(lose_list)

for lp3 in range(count):
    for lp4 in lose_list:
        print(lp3 + 1)
        print((lp3 + 1) in lp4)
    print("")

