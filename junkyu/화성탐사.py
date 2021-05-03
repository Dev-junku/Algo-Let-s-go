import sys
from heapq import heappop, heappush

sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    global q, graph, mapping

    while q:
        x, y, dist = heappop(q)

        if mapping[x][y] < dist:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                cost = dist + graph[nx][ny]
                if cost < mapping[nx][ny]:
                    mapping[nx][ny] = cost
                    heappush(q, (nx, ny, cost))

T = int(input())

for t in range(1, T+1):
    N = int(input())
    INF = int(1e9)
    graph = [list(map(int, input().split())) for _ in range(N)]
    mapping = [[INF]*N for _ in range(N)]
    q = []
    heappush(q, (0, 0, graph[0][0]))
    bfs()
    print(mapping[N-1][N-1])



