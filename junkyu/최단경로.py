from heapq import heappop, heappush

V, E = map(int, input().split())

k = int(input())

INF = int(1e9)

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(s):

    distance = [INF] * (V+1)
    distance[s] = 0

    q = []
    heappush(q, (0, s))

    while q:
        dist, now = heappop(q)

        if distance[now] < dist:
            continue

        for v, u in graph[now]:
            u += dist

            if distance[v] > u:
                distance[v] = u
                heappush(q, (distance[v], v))
    
    return distance

distance = dijkstra(k)
for ans in distance[1:]:
    print(ans) if ans != INF else print('INF') 