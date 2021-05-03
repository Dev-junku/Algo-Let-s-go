import sys
from heapq import heappop, heappush

INF = int(1e9)

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

start, end = map(int, input().split())

def dijkstar(start, end):
    distance = [INF] * (N+1)
    distance[start] = 0

    q = []
    heappush(q, (0, start))

    while q:
        dist, now = heappop(q)

        if distance[now] < dist:
            continue

        for node, cost in graph[now]:
            cost += dist

            if distance[node] > cost:
                distance[node] = cost
                heappush(q, (cost, node))
    
    return distance[end]

print(dijkstar(start, end))
