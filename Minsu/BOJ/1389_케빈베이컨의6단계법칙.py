N, M = map(int, input().split())
friends = [list(map(int, input().split())) for _ in range(M)]

relations = [[99999] * N for _ in range(N)]

# print(friends)
# print(relations)

# 친구관계 그래프
for friend in friends:
    relations[friend[0]-1][friend[1]-1] = 1
    relations[friend[1]-1][friend[0]-1] = 1

# print(relations)

for K in range(N): # 거치는 점
    for i in range(N): # 시작점
        for j in range(N): # 끝점
            # K를 거쳤을 때의 경로가 더 적은 경로
            if relations[i][j] > relations[i][K] + relations[K][j]:
                relations[i][j] = relations[i][K] + relations[K][j]

# print(relations)

minimum = 99999
for i in range(N):
    total = 0
    for j in range(N):
        if i != j:
            total += relations[i][j]
    if minimum > total:
        minimum = total
        min_i = i

print(min_i + 1)