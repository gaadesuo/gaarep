# 騒音の広さの情報の取得
sound = [int(lp) for lp in input().split()]
# print(sound)

# 木陰の場所の数
s_round = int(input())

# 木陰の情報の取得と計算
for lp0 in range(s_round):
    wd_list = [int(lp1) for lp1 in input().split()]
    # print(wd_list)
    num1 = ((wd_list[0] - sound[0]) ** 2)
    num2 = ((wd_list[1] - sound[1]) ** 2)
    num3 = int(sound[2]) ** 2
    # print(num1, num2, num3)
    print("silent"  if num1 + num2 >= num3 else "noisy")