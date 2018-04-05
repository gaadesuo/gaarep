count = 0
for num in range(1, 21):
    if num % 10 == 3 or num % 3 == 0:
        count += 1
        print("{}! {}".format(num, count))
    else:
        print(num)