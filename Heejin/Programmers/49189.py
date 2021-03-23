def solution(n, edge):
    answer = 0
    adj = [[] for _ in range(n+1)]
    dist = [0 for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    for e in edge:
        start = e[0]
        end = e[1]
        adj[start].append(end)
        adj[end].append(start)

    queue = [1]
    visited[1] = True
    while queue:
        current = queue.pop(0)
        for i in adj[current]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                dist[i] = dist[current] + 1

    max_dist = max(dist)
    for i in range(n+1):
        if dist[i] == max_dist:
            answer += 1

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))