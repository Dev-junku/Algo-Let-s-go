N = int(input())                                          # 회원 수
dist = [[N+1 for _ in range(N+1)] for _ in range(N+1)]    # i번에서 j번까지의 친구 거리 기록

# 회원 친구 기록: -1, -1이 나올 때까지
while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    else:
        dist[a][b] = 1
        dist[b][a] = 1

# 자기 자신과의 거리는 0
for i in range(N+1):
    dist[i][i] = 0

# 플로이드-워셜
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                dist[j][i] = dist[i][k] + dist[k][j]


maximums = [max(dist[i][1:]) for i in range(N+1)]                           # 회원 점수
min_score = min(maximums)                                                   # 회장 후보의 점수
candidates = [str(i) for i in range(1, N+1) if maximums[i] == min_score]    # 회장 후보

print(min_score, len(candidates))
print(' '.join(candidates))
