# データ入力
inp_num = [int(lp0) for lp0 in input().split()]
# print("機械の数とお菓子の数")
# print(inp_num)

# 機械ごとの箱の数の入力と計算
box = []
ans = []
index = []
for lp0 in range(inp_num[0]):
    box.append(int(input()))
    ans.append(inp_num[1] % box[lp0])
print(box)
print(ans)

# あまりが最小の機械のインデックスの検索
ans_list = []
c_num = 0
for lp1 in ans:
    if lp1 == min(ans):
        index.append(c_num)

    c_num += 1
print(index)
for lp2 in index:
    ans_list.append(box[lp2])
print(ans_list)

# 表示
print((box.index(max(ans_list))) + 1)