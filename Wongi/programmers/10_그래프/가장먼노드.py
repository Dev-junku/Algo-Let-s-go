def solution(n, edge):
    G = [[] for _ in range(n+1)]
    for e in edge:
        v, u = e
        G[v].append(u)
        G[u].append(v)

    visited = [0] * (n + 1)
    dist = [0] * (n + 1)
    Q = [1]
    visited[1] = 1
    dist[1] = 0
    max_cnt = 0
    while Q:
        cur_n = Q.pop(0)
        if max_cnt < dist[cur_n]:
            max_cnt = dist[cur_n]

        for adj in G[cur_n]:
            if not visited[adj]:
                visited[adj] = 1
                dist[adj] = dist[cur_n] + 1
                Q.append(adj)

    return dist.count(max_cnt)


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))