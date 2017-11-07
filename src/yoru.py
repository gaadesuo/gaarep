# ***データ入力***
num_list = []
all_num_list =[]
inp_num = int(input())
for lp0 in range(inp_num):
    inp_num_list = [int(num) for num in input().split()]
    for lp1 in inp_num_list:
        all_num_list.append(lp1) # 入力された数字の確認用リスト
    num_list.append(inp_num_list)
all_num_list.sort()
print("入力された行毎のリスト " + str(num_list))
# print("入力された数字のリスト" + str(all_num_list))

# ***処理***
count_nums = [num for num in range(1, (inp_num ** 2) + 1)]
# print("数字確認用リスト" + str(count_nums))
for num in all_num_list:
    if num in count_nums:
        count_nums.remove(num)
print("入力されていない数字は" + str(count_nums))
max_num = int((((inp_num ** 3) - inp_num) / 2) + inp_num)
print("各行の計算した値は" + str(max_num))
next_list =[]
for nums in num_list: # 横の行から入る数字を求める
    if nums.count(0) == 1: # 横の行で0が一つなら求められる
        ans_num = max_num - sum(nums)
        count_nums.remove(ans_num)
        nums[nums.index(0)] = ans_num # 0のインデックスの場所に答えを代入
    next_list.append((nums))
print("横の行で計算して求めた後のリスト" + str(next_list))
if len(count_nums) > 0:
    ans_list = []
    for lp2 in range(inp_num):
        total_num = 0
        for lists in next_list: # リストの同一インデックスの数字を足していく
            total_num += lists[lp2]
        if total_num != max_num:
            index_num = next_list.index(lists)
            # ここを関数化できるか？
            ans_num = max_num - total_num
            count_nums.remove(ans_num)
            lists[lists.index(0)] = ans_num
            next_list[index_num] = lists

for w_list in next_list:
    str_list = map(str, w_list)
    print(" ".join(str_list))