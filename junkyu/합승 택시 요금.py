import heapq

INF = int(1e9)
graph = [[]]

def make_edge(n, fares):
    global graph

    graph = [[] for i in range(n+1)]

    for fare in fares:
        start, end, cost = fare[0], fare[1], fare[2]
        graph[start].append([end, cost])
        graph[end].append([start, cost])


def dijkstra(s, e):
    global graph

    num = len(graph)
    distance = [INF for i in range(num)]
    distance[s] = 0

    q = [[0, s]]

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue
  
        for v in graph[node]:
            now, cost = v[0], v[1]
            cost += dist

            if cost < distance[now]:
                distance[now] = cost
                heapq.heappush(q, [cost, now])
        
    return distance[e]


def solution(n, s, a, b, fares):
    make_edge(n, fares)
    res_cost = INF
    
    for i in range(1, n+1):
        res_cost = min(res_cost, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))

    return res_cost


if __name__ == '__main__':
    print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
    print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
    print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))