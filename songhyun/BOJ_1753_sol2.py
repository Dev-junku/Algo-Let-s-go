import sys
sys.stdin = open('input.txt')
import heapq

INF = 1000000000
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def djikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    #시작점
    while q:
        dist, now = heapq.heappop(q)
        #여기서 dist는 현재까지 거리
        if distance[now] < dist:
            continue
        #distance가 dist보다 작으면 즉 방문처리
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:de
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

djikstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])