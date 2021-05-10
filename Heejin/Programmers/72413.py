import heapq

def dijkstra(start, n, graph):
    INF = float('inf')
    dist = [INF for _ in range(n+1)]
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        cur_fare, cur_node = heapq.heappop(q)
        for next_node, fare in graph[cur_node]:
            next_fare = cur_fare + fare
            if cur_fare + fare < dist[next_node]:
                dist[next_node] = next_fare
                heapq.heappush(q, (next_fare, next_node))
    return dist

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    s_ = dijkstra(s, n, graph)
    a_ = dijkstra(a, n, graph)
    b_ = dijkstra(b, n, graph)
    min_ = 987654321
    for i in range(1, n+1):
        if s_[i] + a_[i] + b_[i] < min_:
            min_ = s_[i] + a_[i] + b_[i]

    return min_

print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))