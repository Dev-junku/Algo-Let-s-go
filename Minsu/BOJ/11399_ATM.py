N = int(input())
clients = list(map(int, input().split()))

# 걸리는 시간이 작을수록 앞으로 서는게 좋다
# 정렬하기(선택정렬)
for i in range(len(clients)):
    min_index = i
    for j in range(i, len(clients)):
        if clients[min_index] > clients[j]:
            min_index = j
    clients[i], clients[min_index] = clients[min_index], clients[i]

# 시간의 합 구하기
for i in range(1, len(clients)):
    clients[i] = clients[i-1] + clients[i]

total = 0
for i in range(len(clients)):
    total += clients[i]

print(total)