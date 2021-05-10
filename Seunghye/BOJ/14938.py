n, m, r = map(int, input().split())
t = [0] + list(map(int, input().split()))

INF = float('inf')
dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    dist[a][b] = l
    dist[b][a] = l

for i in range(1, n+1):
    dist[i][i] = 0

# 플로이드-와샬
for i in range(n+1):
    for j in range(n+1):
        for k in range(n+1):
            if i != j and i != k and j != k:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    dist[j][i] = dist[i][j]

# m 이하의 범위에 있는 지역을 대상으로, 해당 지역의 아이템 개수를 합하고, 그 중 최대치를 출력
print(max(sum(t[j] for j in range(1, n+1) if dist[i][j] <= m) for i in range(1, n+1)))
