import numpy as np

t_l = []
inp_l = []
big_n = []
small_n = []
divisible = []
s_b_list = []
div_l = []
for i in range(int(input())):
    w = input()
    # print(w)
    t_l = w.split()
    # print(t_l)
    inp_l.append(t_l)
# print(inp_l)

for i in range(len(inp_l)):
    # print(inp_l[i])
    if inp_l[i][0] == ">":
        big_n.append(int(inp_l[i][1]))
    elif inp_l[i][0] == "<":
        small_n.append(int(inp_l[i][1]))
    elif inp_l[i][0] == "/":
        divisible.append(int(inp_l[i][1]))
# print(big_n, small_n,divisible)

b_num = (max(big_n))
s_num = (min(small_n))

for i in range(101):
    if s_num > i > b_num:
        s_b_list.append(i)

# print(s_b_list)

# n_divisible = np.array(divisible)
n_s_b_list = np.array(s_b_list)
print(n_s_b_list)
for i in divisible:
    div = np.where(n_s_b_list % i == 0)[0]
    print(div)
    div_l.append(div)
print(div_l)