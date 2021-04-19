from itertools import permutations

N = int(input())
N_list = list(map(int, input().split()))

# Dat = permutations(N_list, 5)

# min_data = 99999999999999999
# for D in Dat:
#     min_v = []
#     for i in range(1, N+1):
#         min_v.append(sum(D[:i]))
#         if sum(min_v) > min_data:
#             break
#     if min_data > sum(min_v):
#         min_data = sum(min_v)
# print(min_data)

new_list = []
while N_list:
    dat = min(N_list)
    new_list.append(dat)
    N_list.remove(min(N_list))
# print(new_list)

res = 0
for i in range(1, N+1):
    res += sum(new_list[:i])
print(res)




